words = '\033[31mAPRENDER\033[m', '\033[31mPROGRAMAR\033[m', '\033[31mLINGUAGEM\033[m',\
        '\033[31mPYTHON\033[m', '\033[31mCURSO\033[m', '\033[31mGRATIS\033[m', \
        '\033[31mESTUDAR\033[m', '\033[31mPRATICAR\033[m', '\033[31mTRABALHAR\033[m',\
        '\033[31mMERCADO\033[m', '\033[31mPROGRAMADOR\033[m', '\033[31mFUTURO\033[m'
print('-' *40)
for p in words:
    print(f'\nNa palvavra {p} temos ', end='')
    for c in p:
        if c in 'AEIOU':
            print(c, end=' ')
print('\n')
print('-' * 40)
