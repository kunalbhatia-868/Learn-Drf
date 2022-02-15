from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size=1         #give pages on /?page=2 or 3 to chnage it use params
    page_query_param='p' # give pages on /?p=2 or 3 
    page_size_query_param='size'       #to change page size from client side in urls
    max_page_size=2                     #to set limit page size control from client
    #to load last /?page p=last
    last_page_strings="end"     #to chnage last page name