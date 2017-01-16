from csv import DictReader
import os

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

import odatagym_app.settings as ods

import logging
logger = logging.getLogger('odata_gym')


class DatasetsHandler(ViewSet):
    def get(self, request, dataset_folder, dataset_name, format=None):
        DELIMITERS_MAP = {
            'c': ',',
            'sc': ';',
            'sp': ' '
        }

        dataset_path = os.path.join(ods.DATASETS_DIR, dataset_folder, dataset_name)
        print dataset_path
        if os.path.exists(dataset_path):
            print request.query_params
            delimiter = request.GET.get('file_delimiter', 'c')
            print 'Delimiter is %s' % delimiter
            with open(dataset_path) as dataset:
                reader = DictReader(dataset, delimiter=DELIMITERS_MAP[delimiter])
                data = [x for x in reader]
                return Response(data, status=status.HTTP_200_OK)
        else:
            raise NotFound('There is no dataset %s for %s' % (dataset_name, dataset_folder))
