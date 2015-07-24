# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import math
ENG_KEY = u"rRseEfaqQtTdwWczxvgkoiOjpuPhynbml";
KOR_KEY = u"ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ";
CHO_DATA = u"ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ";
JUNG_DATA = u"ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ";
JONG_DATA = u"ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ";

def engTypeToKor(src) :
    res = "";
    if (len(src)== 0):
        return res;

    nCho = -1
    nJung = -1
    nJong = -1;      # 초성, 중성, 종성

    for  i in range(len( src)) :
        ch = src[i];
        p = ENG_KEY.find(ch);
        if (p == -1)   :            # 영자판이 아님
            # 남아있는 한글이 있으면 처리
            if (nCho != -1) :
                if (nJung != -1)  :              # 초성+중성+(종성)
                    res += makeHangul(nCho, nJung, nJong);
                else :                            # 초성만
                    res += CHO_DATA[nCho];
            else : 
                if (nJung != -1)   :             # 중성만
                    res += JUNG_DATA[nJung];
                elif (nJong != -1)   :        # 복자음
                    res += JONG_DATA[nJong];
            
            nCho = -1;
            nJung = -1;
            nJong = -1;
            res += ch;
        elif (p < 19)  :           # 자음
            if (nJung != -1) :
                if (nCho == -1)   :                 # 중성만 입력됨, 초성으로
                    res += JUNG_DATA[nJung];
                    nJung = -1;
                    nCho = CHO_DATA.find(KOR_KEY[p]);
                else :                             # 종성이다
                    if (nJong == -1)   :            # 종성 입력 중
                        nJong = JONG_DATA.find(KOR_KEY[p]);
                        if (nJong == -1)  :         # 종성이 아니라 초성이다
                            res += makeHangul(nCho, nJung, nJong);
                            nCho = CHO_DATA.find(KOR_KEY[p]);
                            nJung = -1;
                        
                    elif (nJong == 0 and p == 9)  :         # ㄳ
                        nJong = 2;
                    elif (nJong == 3 and p == 12)  :        # ㄵ
                        nJong = 4;
                    elif (nJong == 3 and p == 18)  :        # ㄶ
                        nJong = 5;
                    elif (nJong == 7 and p == 0)   :        # ㄺ
                        nJong = 8;
                    elif (nJong == 7 and p == 6)   :        # ㄻ
                        nJong = 9;
                    elif (nJong == 7 and p == 7)   :        # ㄼ
                        nJong = 10;
                    elif (nJong == 7 and p == 9)   :        # ㄽ
                        nJong = 11;
                    elif (nJong == 7 and p == 16)  :        # ㄾ
                        nJong = 12;
                    elif (nJong == 7 and p == 17)  :        # ㄿ
                        nJong = 13;
                    elif (nJong == 7 and p == 18)   :       # ㅀ
                        nJong = 14;
                    elif (nJong == 16 and p == 9)   :       # ㅄ
                        nJong = 17;
                    else :                         # 종성 입력 끝, 초성으로
                        res += makeHangul(nCho, nJung, nJong);
                        nCho = CHO_DATA.find(KOR_KEY[p]);
                        nJung = -1;
                        nJong = -1;
                    
                
            else :                                 # 초성 또는 (단/복)자음이다
                if (nCho == -1)  :                  # 초성 입력 시작
                    if (nJong != -1)     :          # 복자음 후 초성
                        res += JONG_DATA[nJong];
                        nJong = -1;
                    
                    nCho = CHO_DATA.find(KOR_KEY[p]);
                elif (nCho == 0 and p == 9) :           # ㄳ
                    nCho = -1;
                    nJong = 2;
                elif (nCho == 2 and p == 12) :          # ㄵ
                    nCho = -1;
                    nJong = 4;
                elif (nCho == 2 and p == 18) :          # ㄶ
                    nCho = -1;
                    nJong = 5;
                elif (nCho == 5 and p == 0) :           # ㄺ
                    nCho = -1;
                    nJong = 8;
                elif (nCho == 5 and p == 6)   :         # ㄻ
                    nCho = -1;
                    nJong = 9;
                elif (nCho == 5 and p == 7)    :        # ㄼ
                    nCho = -1;
                    nJong = 10;
                elif (nCho == 5 and p == 9)  :          # ㄽ
                    nCho = -1;
                    nJong = 11;
                elif (nCho == 5 and p == 16)  :         # ㄾ
                    nCho = -1;
                    nJong = 12;
                elif (nCho == 5 and p == 17)  :         # ㄿ
                    nCho = -1;
                    nJong = 13;
                elif (nCho == 5 and p == 18)   :        # ㅀ
                    nCho = -1;
                    nJong = 14;
                elif (nCho == 7 and p == 9)  :          # ㅄ
                    nCho = -1;
                    nJong = 17;
                else :                             # 단자음을 연타
                    res += CHO_DATA[nCho];
                    nCho = CHO_DATA.find(KOR_KEY[p]);
                
            
        else :                                     # 모음
            if (nJong != -1)    :                   # (앞글자 종성), 초성+중성
                # 복자음 다시 분해
                newCho=-1;         # (임시용) 초성
                if (nJong == 2)   :                 # ㄱ, ㅅ
                    nJong = 0;
                    newCho = 9;
                elif (nJong == 4) :            # ㄴ, ㅈ
                    nJong = 3;
                    newCho = 12;
                elif (nJong == 5)   :          # ㄴ, ㅎ
                    nJong = 3;
                    newCho = 18;
                elif (nJong == 8)  :           # ㄹ, ㄱ
                    nJong = 7;
                    newCho = 0;
                elif (nJong == 9)  :           # ㄹ, ㅁ
                    nJong = 7;
                    newCho = 6;
                elif (nJong == 10)  :          # ㄹ, ㅂ
                    nJong = 7;
                    newCho = 7;
                elif (nJong == 11)  :          # ㄹ, ㅅ
                    nJong = 7;
                    newCho = 9;
                elif (nJong == 12)   :         # ㄹ, ㅌ
                    nJong = 7;
                    newCho = 16;
                elif (nJong == 13)   :         # ㄹ, ㅍ
                    nJong = 7;
                    newCho = 17;
                elif (nJong == 14)    :        # ㄹ, ㅎ
                    nJong = 7;
                    newCho = 18;
                elif (nJong == 17)   :         # ㅂ, ㅅ
                    nJong = 16;
                    newCho = 9;
                else :                             # 복자음 아님
                    newCho = CHO_DATA.find(JONG_DATA[nJong]);
                    nJong = -1;
                
                if (nCho != -1)  :       # 앞글자가 초성+중성+(종성)
                    res += makeHangul(nCho, nJung, nJong);
                else :                    # 복자음만 있음
                    res += JONG_DATA[nJong];

                nCho = newCho;
                nJung = -1;
                nJong = -1;
            
            if (nJung == -1)     :                  # 중성 입력 중
                nJung = JUNG_DATA.find(KOR_KEY[p]);
            elif (nJung == 8 and p == 19)  :           # ㅘ
                nJung = 9;
            elif (nJung == 8 and p == 20)  :           # ㅙ
                nJung = 10;
            elif (nJung == 8 and p == 32)  :           # ㅚ
                nJung = 11;
            elif (nJung == 13 and p == 23) :           # ㅝ
                nJung = 14;
            elif (nJung == 13 and p == 24) :           # ㅞ
                nJung = 15;
            elif (nJung == 13 and p == 32)  :          # ㅟ
                nJung = 16;
            elif (nJung == 18 and p == 32)   :         # ㅢ
                nJung = 19;
            else :             # 조합 안되는 모음 입력
                if (nCho != -1)    :        # 초성+중성 후 중성
                    res += makeHangul(nCho, nJung, nJong);
                    nCho = -1;
                else :                      # 중성 후 중성
                    res += JUNG_DATA[nJung];
                nJung = -1;
                res += KOR_KEY[p];
            
        
    

    # 마지막 한글이 있으면 처리
    if (nCho != -1) :
        if (nJung != -1)   :         # 초성+중성+(종성)
            res += makeHangul(nCho, nJung, nJong);
        else :                        # 초성만
            res += CHO_DATA[nCho];
    else : 
        if (nJung != -1)       :     # 중성만
            res += JUNG_DATA[nJung];
        else :                       # 복자음
            if (nJong != -1):
                res += JONG_DATA[nJong];
        
    

    return res;


def makeHangul(nCho, nJung, nJong) :
    return unichr(0xac00 + nCho * 21 * 28 + nJung * 28 + nJong + 1);


def korTypeToEng(src) :
    res = "";
    if ( len(src) == 0):
        return res;

    for i in range( len( src)) :
        ch = src[i];
        nCode = ord(unicode(ch) )

        nCho = CHO_DATA.find(ch)
        nJung = JUNG_DATA.find(ch)
        nJong = JONG_DATA.find(ch);
        arrKeyIndex = [-1, -1, -1, -1, -1];

        if (0xac00 <= nCode and nCode <= 0xd7a3) :
            nCode -= 0xac00;
            arrKeyIndex[0] = int(math.floor(nCode / (21.0 * 28)));         # 초성

            arrKeyIndex[1] =  int(math.floor( nCode / 28.0 )) % 21;           # 중성
            arrKeyIndex[3] = nCode % 28 - 1;                        # 종성
        elif (nCho != -1)     :     # 초성 자음
            arrKeyIndex[0] = nCho;
        elif (nJung != -1)    :       # 중성
            arrKeyIndex[1] = nJung;
        elif (nJong != -1)      :     # 종성 자음
            arrKeyIndex[3] = nJong;
        else :                            # 한글이 아님
            res += ch;

        # 실제 Key Index로 변경. 초성은 순서 동일
        if (arrKeyIndex[1] != -1) :
            if (arrKeyIndex[1] == 9) :                  # ㅘ
                arrKeyIndex[1] = 27;
                arrKeyIndex[2] = 19;
            elif (arrKeyIndex[1] == 10)   :        # ㅙ
                arrKeyIndex[1] = 27;
                arrKeyIndex[2] = 20;
            elif (arrKeyIndex[1] == 11) :          # ㅚ
                arrKeyIndex[1] = 27;
                arrKeyIndex[2] = 32;
            elif (arrKeyIndex[1] == 14)  :         # ㅝ
                arrKeyIndex[1] = 29;
                arrKeyIndex[2] = 23;
            elif (arrKeyIndex[1] == 15)   :        # ㅞ
                arrKeyIndex[1] = 29;
                arrKeyIndex[2] = 24;
            elif (arrKeyIndex[1] == 16)   :        # ㅟ
                arrKeyIndex[1] = 29;
                arrKeyIndex[2] = 32;
            elif (arrKeyIndex[1] == 19)  :         # ㅢ
                arrKeyIndex[1] = 31;
                arrKeyIndex[2] = 32;
            else :                
                arrKeyIndex[1] = KOR_KEY.find( JUNG_DATA[   arrKeyIndex[1]  ] );
                arrKeyIndex[2] = -1;
            

        if (arrKeyIndex[3] != -1) :
            if (arrKeyIndex[3] == 2)    :               # ㄳ
                arrKeyIndex[3] = 0
                arrKeyIndex[4] = 9;
            elif (arrKeyIndex[3] == 4) :           # ㄵ
                arrKeyIndex[3] = 2;
                arrKeyIndex[4] = 12;
            elif (arrKeyIndex[3] == 5) :           # ㄶ
                arrKeyIndex[3] = 2;
                arrKeyIndex[4] = 18;
            elif (arrKeyIndex[3] == 8) :           # ㄺ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 0;
            elif (arrKeyIndex[3] == 9)  :          # ㄻ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 6;
            elif (arrKeyIndex[3] == 10)   :        # ㄼ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 7;
            elif (arrKeyIndex[3] == 11)   :        # ㄽ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 9;
            elif (arrKeyIndex[3] == 12)     :      # ㄾ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 16;
            elif (arrKeyIndex[3] == 13)  :         # ㄿ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 17;
            elif (arrKeyIndex[3] == 14)   :        # ㅀ
                arrKeyIndex[3] = 5;
                arrKeyIndex[4] = 18;
            elif (arrKeyIndex[3] == 17)  :         # ㅄ
                arrKeyIndex[3] = 7;
                arrKeyIndex[4] = 9;
            else : 
                arrKeyIndex[3] = KOR_KEY.find(JONG_DATA[arrKeyIndex[3]]);
                arrKeyIndex[4] = -1;   
        

        for j in range(5): 
            if (arrKeyIndex[j] != -1):
                res += ENG_KEY[arrKeyIndex[j]];    

    return res;


def isEnglish(src):
    for ch in src:
        ch_unicode = ord(unicode(ch))
        if  not ( 0<=ch_unicode<=0x7f ) :
            return False
    return True

def isKorean(src):
    for ch in src:
        ch_unicode = ord(unicode(ch))
        if  not ( (0xAC00<=ch_unicode<=0xD7AF) or (0x3131<=ch_unicode<=0x3163) or ch==' ' ) :
            return False
    return True


def trans(src):
    if isEnglish(src):
        return engTypeToKor(src)
    if isKorean(src):
        return korTypeToEng(src)
    return "Input Korean or English"



if __name__ == '__main__' :
    # print korTypeToEng(u'하이데어')
    # print engTypeToKor(u'gkdlepdj')
    # print ord(unicode(u'가') )
    # print isEnglish(u'src가')
    print TypeTo(u"tjfgus")
    # for c in JONG_DATA:`
    #     print hex(ord(unicode(c))) # 0x3131~0x314e

    # for c in JUNG_DATA:
    #     print hex(ord(unicode(c))) # 0x314f~0x3163