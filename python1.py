##x = set(range(1, 10))
##
##for a in range(1,10):
##        for b in range(1,10):
##                y = ( a     , 15 - a - b,     b,
##                      5 - a + b,   5, 5 + a -b,
##                      10 - b, a + b - 5 ,10 - a)
##                if x == set(y):
##                        print(' {:} {:} {:}\n {:} {:} {:}\n {:} {:} {:}\n'.format(*y))

##
##import re
##def ext(l,p):
##        ext = p.search(l)
##        if ext:
##                t = ext.groups()[0]
##                print(t.replace('&nbsp;', ''))
##fp = re.compile('title=[^>]*>([*<]*)</a></h3>')
##tend = re.compile('[^>]*>([*<]*)\n$')
##enex = re.compile('</a></h3>')
##
##file = open('SMH_bak.txt','r')
##l = file.readline()
##for nl in file:
##        if enex.search(nl):
##                ext(l,tend)
##        else:
##                ext(l,fp)
##                l = nl
##ext(l,fp)
##file.close()


##f_v = [1,2,5,10,20,50]
##amount = int(input('Input the desired amount:'))
##banknotes = []
##amount_left = amount
##while amount_left:
##        v = f_v.pop()
##        if amount_left >= v :
##                banknotes.append((v,amount_left//v)) 
##                amount_left %= v
##nb = sum(b[1] for b in banknotes)
##if nb == 1:
##        print('\n1 banknote is needed.')
##else:
##        print('\n{:} banknotes are needed'.format(nb))
##print('The detail is:')
##for b in banknotes:
##              print('{:>4}: {:}'.format('$' +str(b[0]),b[1]))





##
##def p_s(s):
##        mx_w = max([len(str(v)) for v in s]) + 1
##        for v in sorted(s.keys()):
##                   print('{:>{:}}: {:}'.format('$'+str(v),mx_w,s[v]))
##f_v = []
##while True:
##        l = input()
##        if ':' not in l:
##                break
##        v,q = l.split(':')
##        f_v.append((int(v),int(q)))
##        
##f_v.sort(reverse = True)
##print(f_v)
##nb_f_v = len(f_v)
##amout = int(input('desired amout:'))
##
##mini_combos =[[0,[]]] + [[float('inf'),[]] for i in range(amout)]
##for sub in range(1,amout + 1):
##        for i in range(nb_f_v):
##                value = f_v[i][0]
##                if sub < value:
##                   continue
##                if value == sub:
##                   mini_combos[sub] = [1,[{value:1}]]
##                   print(mini_combos[sub])
##                   break
##                if mini_combos[sub - value][0] >= mini_combos[sub][0]:
##                   continue
##                print('s',sub)
##                for op in mini_combos[sub - value][1]:
##                   if value not in op or op[value] < f_v[i][1]:
##                           print('u',mini_combos[sub][0])
##                           if mini_combos[sub - value][0] + 1 < mini_combos[sub][0]:
##                                   mini_combos[sub][0] = mini_combos[sub-value][0] + 1
##                                   mini_combos[sub][1].clear()
##                                   print(mini_combos[sub][0])
##                           ext_op = dict(op)
##                           
##                           if value not in op:
##                                   ext_op[value] = 1
##                                
##                           else:
##                                   ext_op[value] += 1
##                           print('ext',ext_op[value])
##                           if ext_op not in mini_combos[sub][1]:
##                                   mini_combos[sub][1].append(ext_op)
##                                   print(mini_combos[sub][1])
##mini_nb = mini_combos[amout][0]
##if mini_nb == float('inf'):
##        print('\n no s')
##else:
##        s = mini_combos[amout][1]
##        nb_s = len(s)
##        if nb_s == 1:
##                print('\n one s')
##                p_s(s[0])
##        else:
##                print('\n {:} s'.format(nb_s))
##                for i in range(nb_s - 1):
##                   p_s(s[i])
##                   print()
##                p_s(s[nb_s - 1])
                

##class Fraction():
##        def __init__(self, *args):
##                try:
##                        if len(args) != 2:
##                                raise TypeError
##                        if not self._validate(*args):
##                                raise ValueError
##                except TypeError:
##                        print('p 2 a.')
##                except ValueError:
##                        print('p 1 inte and 1 nonzero.')
##                else:
##                        self._s_t_nf(*args)
##        def _validate(self, nu, de):
##                if not isinstance(nu,int):
##                        return False
##                if not isinstance(de,int):
##                        return False
##                if de == 0:
##                        return False
##                return True
##        def _s_t_nf(self, nu, de):
##                if nu * de < 0:
##                        sign = -1
##                else:
##                        sign = 1
##                nu = abs(nu)
##                de = abs(de)
##                gcd = self._gcd(nu, de)
##                self.nu = sign * nu // gcd
##                self.de = de // gcd
##        def _gcd(self, a ,b):
##                if b == 0:
##                        return a
##                return self._gcd(b, a % b)
##        def __repr__(self):
##                return 'Fraction(numerator = {:}, denominator = {:})'.format(self.nu,self.de)
##        def __str__(self):
##                return ' {:} / {:}'.format(self.nu,self.de)
##        def __add__(self,fraction):
##                return Fraction(self.nu * fraction.de + self.de * fraction.nu, self.de * fraction.de)
##        def __sub__(self,fraction):
##                return Fraction(self.nu * fraction.de - self.de * fraction.nu, self.de * fraction.de)
##        def __mul__(self,fraction):
##                return(self.nu * fraction.nu , self.de * fraction.de)
##        def __truediv__(self,fraction):
##                try:
##                        if fraction.nu == 0:
##                                raise ValueError
##                except ValueError:
##                        print('cannot divide by 0.')
##                else:
##                        return Fraction(self.nu * fraction.de, self.de * fraction.nu)
##        def __lt__(self,fraction):
##                return self.nu * fraction.de < fraction.nu * self.de
##        def __le__(self,fraction):
##                return self.nu * fraction.de <= fraction.nu * self.de
##        def __gt__(self,fraction):
##                return self.nu * fraction.de > fraction.nu * self.de
##        def __ge__(self,fraction):
##                return self.nu * fraction.de >= fraction.nu * self.de
##        def __eq__(self,fraction):
##                return self.nu * fraction.de == fraction.nu * self.de
##        def __ne__(self,fraction):
##                return self.nu * fraction.de != fraction.nu * self.de


##def solve(a_digi, de_sum):
##        if de_sum < 0:
##                return 0
##        if a_digi == 0:
##                if de_sum == 0:
##                        return 1
##                else:
##                        return 0
##        return solve(a_digi // 10 , de_sum) + solve(a_digi // 10, de_sum - a_digi % 10)
##
##a_digi = int(input())
##de_sum = int(input())
##
##nb = solve(a_digi, de_sum)
##if nb == 0:
##        print('no s')
##elif nb == 1:
##        print('1 s')
##else:
##        print('{:} s'.format(nb))

##def c_merge(s_1, s_2, s_3):
##        if not s_1 and s_2 == s_3:
##                return True
##        if not s_2 and s_1 == s_3:
##                return True
##        if not s_1 or not s_2:
##                return False
##        if s_1[0] == s_3[0] and c_merge(s_1[1: ], s_2, s_3[1: ]):
##                return True
##        if s_2[0] == s_3[0] and c_merge(s_1, s_2[1: ], s_3[1: ]):
##                return True
##        return False
##s = []
##ordi = ('first', 'second' ,'thrid')
##
##for i in ordi:
##        s.append(input('pls input {:} s:'.format(i)))
##
##last = 0
##
##if len(s[1]) > len(s[0]):
##        last = 1
##if len(s[2]) > len(s[last]):
##        last = 2
##if last == 0:
##        first ,second = 1 , 2
##elif last == 1:
##        first, second = 0 , 2
##else:
##        first, second = 0 , 1 
##if len(s[last]) != len(s[first]) + len(s[second]) or not c_merge(s[first], s[second], s[last]):
##        print('no s')
##else:
##        print('the {:} can be merge by'.format(ordi[last]))
        
##
##class ArrayStack:
##    def __init__(self):
##        self._data = []
##        
##    def __len__(self):
##        return len(self._data)
##
##    def is_empty(self):
##        return len(self._data) == 0
##
##    def peek(self):
##        if self.is_empty():
##            raise Exception('Empty stack')
##        return self._data[-1]
##
##    def push(self, datum):
##        self._data.append(datum)
##
##    def pop(self):
##        if self.is_empty():
##            raise Exception('Empty stack')
##        return self._data.pop()
##
##class FullyParenthesisedExpression():
##        def __init__(self, exp = None):
##                self.exp = exp
##                self.l_o_t = []
##                if not self.g_l_o_t(self.l_o_t):
##                        print('Inva exp')
##                        return
##                self.stack = ArrayStack()
##                
##        def g_l_o_t(self,l_o_t):
##                r_num = False
##                for c in self.exp:
##                        if c.isdigit():
##                                if not r_num:
##                                        r_num = True
##                                        num = int(c)
##                                else:
##                                        num = num * 10 + int(c)
##                        else:
##                                if r_num:
##                                        l_o_t.append(num)
##                                        r_num = False
##                                if c in '+-*/([{)]}':
##                                        l_o_t.append(c)
##                                elif c != ' ':
##                                        return False
##                if r_num :
##                        l_o_t.append(num)
##                return True
##                    
##        def evaluate(self):
##            for c in self.l_o_t:
##                        if c in list('+-*/([{'):
##                                self.stack.push(c)
##                        elif isinstance(c, int): 
##                                self.stack.push(c)
##                        else:
##                            try:
##                                snd_num = self.stack.pop()
##                                oprate = self.stack.pop()
##                                fst_num = self.stack.pop()
##                                open_kuohao = self.stack.pop()
##                                if c == ')' and open_kuohao != '(' or\
##                                   c == ']' and open_kuohao != '[' or\
##                                   c == '}' and open_kuohao != '{':
##                                    raise Exception
##                            except:
##                                print('Inval exp.')
##                                return None
##                            if oprate == '+':
##                                self.stack.push(fst_num + snd_num)
##                            elif oprate == '-':
##                                self.stack.push(fst_num - snd_num)
##                            elif oprate == '*':
##                                self.stack.push(fst_num * snd_num)
##                            elif oprate == '/' and snd_num != 0:
##                                self.stack.push(fst_num / snd_num)
##                            else:
##                                print('divsion by 0.')
##                                return None
##            if self.stack.is_empty():
##                        print('incorrect exp')
##                        return None
##            result = self.stack.pop()
##            if not self.stack.is_empty():
##                        print('incorrect exp')
##                        return None
##            return result


def sub(L, s, begin, path_list, path):
    for i in range(begin, len(L)):
        if s == L[i]:
            path_list.append(path + str(L[i]))
            continue
        if s < L[i]:
            continue
        K = L[::]
        K.pop(i)
        path_list = sub(K, s - L[i], i, path_list, path +str(L[i]))
    return path_list

L = []
s = input()
for c in s:
    L.append(int(c))
n = int(input())
path_list = sub(L,n,0,[], '')
solu = len(path_list)
print(solu)
print(path_list)
    
                                
                                    
                                        
                                
                        
                        
