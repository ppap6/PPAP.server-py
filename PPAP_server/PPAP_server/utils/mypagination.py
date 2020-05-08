from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_num'
    page_size_query_param = 'page_size'
    max_page_size = 10

    # 重写分页返回方法，按照指定的字段进行分页数据返回
    def get_paginated_response(self, data):
        return Response({
            "status": 200,
            "message":{
            "list":data,#用户数据
            "page_num":self.page.number,#当前页
            "total":self.page.paginator.count,
            "page_size":self.page.paginator.num_pages#总页数
        }}, status=status.HTTP_200_OK)
