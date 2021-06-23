import pandas as pd
import numpy as np
from icecream import ic


if __name__ == '__main__':
    while 1:
        menu = input('2. 판다스 버전 체크하기\n'
                     '3. 판다스 라이브러리 버전 정보 모두 출력하기\n'
                     '4. 주어진 값으로 DataFrame 객체를 생성하시오\n'
                     '5. 객체내부 정보를 출력하시오\n'
                     '6. 객체 상위 3열까지 출력하시오\n'
                     '7. animal과 age 칼럼만 출력하시오\n'
                     '8. 객체의 3,4,8번 인덱스에 해당하는 animal과 age 값 출력\n'
                     '9. visit 컬럼에서 3 초과하는 값 출력\n'
                     '10. age 에서 NaN 값 출력\n'
                     '11. age가 3살 미만 고양이값 출력\n'
                     '12. age가 2살이상 4살 미만인 값 출력\n'
                     '13. f 행의 나이를 1.5살로 변경\n'
                     '14. 객체에서 visit의 합 출력\n'
                     '15. 동물별로 나이의 평균 출력\n'
                     '16. k행을 추가하여 dog, 5.5세, priority: no, visit: 2 내용의 행추가\n'
                     '16-1. 16번 행 삭제\n'
                     '17. 객체에 있는 동물의 종류 수 출력\n'
                     '18. age는 내림차순, visits는 오름차순으로 정렬\n'
                     '19. priority의 yse를 True, no를 False로 맵핑 후 출력\n'
                     '20. snake를 python 으로 값 변경\n'
                     '21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.\n'
                     '번호입력: ')
        if menu == '0':
            break
        elif menu == '2':
            ic(pd.__version__)
        elif menu == '3':
            ic(pd.show_versions())
        elif menu == '4':
            data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
            labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

            df = pd.DataFrame(data=data, index=labels)
            ic(df)
        elif menu == '5':
            ic(df.describe())
        elif menu == '6':
            ic(df.head(3))
        elif menu == '7':
            ic(df.loc[:, 'animal':'age'])
        elif menu == '8':
            ic(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])
        elif menu == '9':
            ic(df[df['visits'] > 2])
        elif menu == '10':
            ic(df[df['age'].isnull()])
        elif menu == '11':
            ic(df[(df['animal']=='cat') & (df['age'] < 3)])
        elif menu == '12':
            ic(df[(df['age'] > 2) & (df['age'] < 4)])
        elif menu == '13':
            df.loc['f', 'age'] = 1.5
            ic(df)
        elif menu == '14':
            ic(df['visits'].sum())
        elif menu == '15':
            ic(df.groupby('animal')['age'].mean())
        elif menu == '16':
            df.loc['k'] = ['dog', '5.5', '2', 'no']
            ic(df)
        elif menu == '16-1':
            ic(df.drop('k', inplace=True))
        elif menu == '17':
            ic(df['animal'].value_counts())
        elif menu == '18':
            ic(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
        elif menu == '19':
            df['priority'] = df['priority'].map({'yes': True, 'no': False})
            ic(df)
        elif menu == '20':
            df['animal'] = df['animal'].replace('snake', 'python')
            ic(df)
        elif menu == '21':
            df = df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
            ic(df)
        else:
            ic('잘못 입력')


def quiz_2():
    pass


