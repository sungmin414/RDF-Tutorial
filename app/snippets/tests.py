import json

from django.test import TestCase
from django.utils.crypto import random
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snippet


class SnippetListTest(APITestCase):
    """
    Snippet List 요청에 대한 테스트
    """
    def test_status_code(self):
        """
        요청 결과의 HTTP 상태코드가 200인지 확인
        :return:
        """
        response = self.client.get('/snippets/django_view/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_snippet_list_count(self):
        """
        Snippet List 를 요청시 DB에 있는 자료수와 같은 갯수가 리턴되는지 확인
        :return:
        """
        for i in range(random.randint(10, 100)):
            Snippet.objects.create(code=f'a = {i}')
        response = self.client.get('/snippets/django_view/snippets/')
        data = json.loads(response.content)

        # response 로 받은 JSON 데이터의 길이와
        # Snippet 테이블의 자료수(count)가 같은지
        self.assertEqual(len(data), Snippet.objects.count())


    def test_snippet_list_order_by_created_descending(self):
        """
        Snippet List 의 결과가 생성일자 내림차순인지 확인
        :return:
        """
        for i in range(random.randint(5, 10)):
            Snippet.objects.create(code=f'a = {i}')
        response = self.client.get('/snippets/django_view/snippets/')
        data = json.loads(response.content)
        # snippets = Snippet.objects.order_by('-created')
        #
        # # response 에 전달된 JSON string 을 파싱한 Python 객체를 순회하며 'pk'값만 꺼냄
        # data_pk_list = []
        # for item in data:
        #     data_pk_list.append(item['pk'])
        #
        # # Snippet.objects.order_by('-created') QuerySet 을 순회하며 각 Snippet 인스턴스의 pk 값만 꺼냄
        # snippets_pk_list = []
        # for snippet in snippets:
        #     snippets_pk_list.append(snippet.pk)

        self.assertEqual(
            # list comprehension
            # data_pk_list,
            # JSON 으로 전달받은 데이터에서 pk만 꺼낸 리스트
            [item['pk'] for item in data],
            # QuerySet.values_list(flat=True)
            # snippets_pk_list,
            # DB 에서 created 역순으로 pk 값만 가져온 QuerySet 으로 만든 리스트
            list(Snippet.objects.order_by('-created').values_list('pk', flat=True))
        )


class SnippetCreateTest(APITestCase):
    def test_snippet_create_status_code(self):
        """
        201이 돌아오는지
        :return:
        """

    def test_snippet_create_save_db(self):
        """
        요청 후 실제 DB 에 저장되었는지 (모든 필드값이 정상적으로 저장되는지)
        :return:
        """

    def test_snippet_create_missing_code_raise_exception(self):
        """
        'code'데이터가 주어지지 않을 경우 적절한 Exception 이 발생하는지
        :return:
        """
