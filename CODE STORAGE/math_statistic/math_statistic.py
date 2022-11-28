'''
Вставить ссылку и понять делал я уже номера из этого варианта или нет.
'''
import requests


def check_if_there_are_no_repeats(url):
    r = requests.get(url)
    st = r.text
    nums_on_this_page = []
    for i in range(st.count('href="/problem?id=')):
        ind = st.find('href="/problem?id=') + len('href="/problem?id=')
        num = ''
        while st[ind].isdigit():
            num += st[ind]
            ind += 1
        nums_on_this_page.append(int(num))
        st = st[ind:]

    norm = True
    for i in open('done_nums.txt'):
        if int(i) in nums_on_this_page:
            norm = False
            print('====', int(i))
    print(*nums_on_this_page, sep='\n')
    print(f'norm = {norm}')


url = input()
check_if_there_are_no_repeats(url)


