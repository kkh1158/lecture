# addr_list = [{'name': 'HONG', 'tel': '1234'},
#              {'name': 'SMITH', 'tel': '8888'},
#              {'name': 'HONG', 'tel': '5678'}]

def addr_file_read():
    rpath="C:\\AI\\pythonProject\\venv\\lecture\\file\\juso.txt"
    with open(file=rpath, mode='r', encoding='UTF-8') as f:
        addr_list=[]
        for line in f.readlines()[1:]:
            dic = {}
            (name_, tel_) = line.split('\t')
            if name_=='' or tel_=='': break
            dic['name'] = name_.replace("\n", "")
            dic['tel'] = tel_.replace("\n", "")
            addr_list.append(dic)
        return addr_list

def addr_file_write(addr_list):
    wpath="C:\\AI\\pythonProject\\venv\\lecture\\file\\juso.txt"
    with open(file=wpath, mode='w', encoding='UTF-8') as f:
        f.write('name' + '\t' + 'tel' + '\n')
        for addr_dic in addr_list:
            if addr_dic['name']=='' or addr_dic['tel']=='': continue
            temp = addr_dic['name'] + '\t' + addr_dic['tel']
            f.write(temp + '\n')

        #f.write(addr_list)

def menu_print():
    print('\t----------------------')
    print('\t1. 추가', '\t2. 수정', '\t3. 삭제')
    print('\t4. 검색', '\t5. 전체', '\t6. 저장')
    print('\t----------------------')

def addr_input(addr_list):
    print('\t******** 추가 ********')
    while True:
        name = input('\t이름: ')
        tel = input('\t번호: ')
        if name!='' and tel!='': break
    dic = {'name': name, 'tel': tel}
    isadd = 0
    for addr_dic in addr_list:
        if dic['tel']==addr_dic['tel']:
            isadd = 1
            break
    if isadd==0:
        addr_list.append(dic)
        print('\t추가 완료')
    elif isadd==1:
        print('\t중복 추가 실패')

def addr_search_all(addr_list):
    print('\t******** 전체 ********')
    for addr_dic in addr_list:
        print('\t', addr_dic['name'], '\t', addr_dic['tel'])
    print('\t총', len(addr_list), '건', end='')
    input('\t아무키 입력')

def addr_search(addr_list):
    print('\t******** 검색 ********')
    input_name = input('\t이름 입력: ')
    search_list=[]
    for addr_dic in addr_list:
        if input_name==addr_dic['name']:
            search_list.append(addr_dic['tel'])
    if len(search_list)==0:
        print('\t검색 결과 없음', end='')
    else:
        for search_tel in search_list:
            print('\t', search_tel)
    input('\t아무키 입력')

def addr_delete(addr_list):
    print('\t******** 삭제 ********')
    input_tel = input('\t번호 입력: ')
    isdel = False
    for i, addr_dic in enumerate(addr_list):  # enumerate() -> 인덱스와 값 리턴
        if input_tel == addr_dic['tel']:
            print('\t', addr_dic['name'], '\t', addr_dic['tel'])
            yn = input('\t정말 삭제합니까?(Y/N)')
            if yn.upper() == 'Y' or yn == '1':
                del addr_list[i]
                isdel = True
    if isdel == True:
        print('\t삭제 완료', end='')
    else:
        print('\t검색 결과 없음', end='')
    # for addr_dic in addr_list:
    #     if input_tel==addr_dic['tel']:
    #         print('\t', addr_dic['name'], '\t', addr_dic['tel'])
    #         yn = input('\t정말 삭제합니까?(Y/N)')
    #         if yn=='Y' or yn=='y' or yn=='1':
    #             addr_list.remove(addr_dic)
    #             print('\t삭제 완료', end='')
    #         else:
    #             print('\t삭제되지않음', end='')
    input('\t아무키 입력')

def addr_update(addr_list):
    print('\t******** 수정 ********')
    input_tel = input('\t번호 입력: ')
    ismod = -1
    for addr_dic in addr_list:
        if input_tel == addr_dic['tel']:
            print('\t', addr_dic['name'], '\t', addr_dic['tel'])
            new_tel = input('\t변경 번호: ')
            for addr_dic2 in addr_list:
                if new_tel == addr_dic2['tel']:
                    ismod = 0
                    break
                else:
                    ismod = 1
    if ismod == 1:
        addr_dic['tel'] = new_tel
        print('\t', addr_dic['name'], '\t', addr_dic['tel'])
        print('\t수정 완료', end='')
    elif ismod == -1:
        print('\t검색 결과 없음', end='')
    elif ismod == 0:
        print('\t중복 번호 수정 실패', end='')
    input('\t아무키 입력')

def juso():
    addr_list = addr_file_read()
    #print(addr_list)
    while True:
        menu_print()
        cmd=input('\t입력: ')
        if cmd == '6':
            print('\t******** 종료 ********')
            addr_file_write(addr_list)
            break
        elif cmd == '1':
            addr_input(addr_list)
        elif cmd == '2':
            addr_update(addr_list)
        elif cmd == '3':
            addr_delete(addr_list)
        elif cmd == '4':
            addr_search(addr_list)
        elif cmd == '5':
            addr_search_all(addr_list)

# 여기 .py에서만 구동
if __name__ == '__main__':
    print('직접돌려보기')
    juso()

# 이건 그냥
# print(addr_list[0])
# print(addr_list[0].keys())          # dict_keys(['name', 'tel'])
# print(list(addr_list[0].keys()))    # ['name', 'tel']
# print(list(addr_list[0].keys())[0]) # name
# print(list(addr_list[0].keys())[1]) # tel