import os
import cx_Oracle
from os.path import isfile, join

def addr_insert_file(path="../file/juso.txt"):
    with open(file=path, mode='r', encoding='UTF-8') as f:
        flist = f.readlines()
        addr_list = []
        dict_key1 = flist[0].strip().split('\t')[0]
        dict_key2 = flist[0].strip().split('\t')[1]
        for line in flist[1:]:
            flist = line.strip().split('\t')
            if len(flist) == 2:
                fdict = {dict_key1:flist[0], dict_key2:flist[1]}
            addr_list.append(fdict)

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :name, :tel)"
    cur = conn.cursor()
    cur.executemany(sql, addr_list)
    conn.commit()
    cur.close()
    conn.close()
    #print(addr_list)
    return len(addr_list)

def addr_insert(prm_name, prm_tel):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel])
    conn.commit()
    cur.close()
    conn.close()

def addr_update(prm_name, prm_tel, prm_seq):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "update addr set name=:1, tel=:2 where seq=:3"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel, prm_seq])
    conn.commit()
    cur.close()
    conn.close()

def addr_delete(prm_seq):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "delete from addr where seq=:1"
    cur = conn.cursor()
    cur.execute(sql, [prm_seq])
    conn.commit()
    cur.close()
    conn.close()

def addr_select():
    conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
    sql = 'select * from addr order by seq'
    cur = conn.cursor()
    cur.execute(sql)
    print('\t seq\t\t name\t\t tel')
    for row in cur:
        rowlist = list(row)
        print('\t', '%-12s%-12s%-15s'%(rowlist[0],rowlist[1],rowlist[2]))
    cur.close()
    conn.close()

def addr_count():
    conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
    sql = 'select count(seq) from addr'
    cur = conn.cursor()
    cur.execute(sql)
    print('\ttotal: ', list(cur)[0][0],)
    cur.close()
    conn.close()

def menu_print():
    print('---------------------------------------------------------------')
    print('\t1. insert\t2. select\t3. delete\t4. update\t5. upfile\t6. exit')
    print('---------------------------------------------------------------')

def juso_db():
    while True:
        menu_print()
        cmd = input('\tplease number: ')
        if cmd=='1':                      # insert
            name = input('\tname?: ')
            tel = input('\ttel?: ')
            addr_insert(name, tel)
            print('\tinsert complete')
        elif cmd=='2':                    # select
            addr_select()
            addr_count()
        elif cmd=='3':                    # delete
            seq = input('\tseq?: ')
            addr_delete(seq)
            print('\tdelete complete')
        elif cmd=='4':                    # update
            seq = input('\tseq?: ')
            name = input('\tname?: ')
            tel = input('\ttel?: ')
            addr_update(name, tel, seq)
            print('\tupdate complete')
        elif cmd=='5':
            dpath = join(os.path.dirname(os.getcwd()), 'file')
            for f in os.listdir(dpath):
                print('\t', f)
            fname = input('\tfile name?')
            fpath = join(dpath, fname)
            if isfile(fpath) :
                cnt = addr_insert_file(fpath)
                print('\t', cnt, 'upload complete')
            else :
                print('\t', fpath, 'is not find')
        elif cmd=='6':
            print('\tTHX')
            break

if __name__ == '__main__':
    juso_db()