'''Import command'''
from api.models import Username
from django.core.management.base import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):
    '''Import command'''
    help = 'Imports usernames into database'

    def add_arguments(self, parser):
        parser.add_argument('input_file')
        parser.add_argument(
            '--batch-size',
            '-b',
            type=int,
            default=10000,
            help='Batch size, higher value for faster import but uses more memory',
        )

    def handle(self, *args, **options):
        with open(options['input_file']) as file_pointer:
            print('Counting number of rows...')
            total = sum(1 for line in file_pointer)
            print(f'{total} lines found.')

        with open(options['input_file']) as file_pointer, tqdm(total=total) as pbar:
            while True:
                objects = []
                size = 0
                for _ in range(options['batch_size']):
                    line = file_pointer.readline().strip()
                    if line == '':
                        break
                    objects.append(Username(username=line))
                    size += 1
                if objects == []:
                    break
                Username.objects.bulk_create(objects, batch_size=size)
                pbar.update(size)
