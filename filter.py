import time
import csv
from math import exp

inputFile = 'data/raw.csv'
outputFile = 'data/data.csv'

class rsxValues():
    
    def __init__(self,v4_,f90_,f88,f8,f28,f30,f38,f40,f48,f50,f58,f60,f68,f70,f78,f80):
        self.v4_ = v4_
        self.f90_ = f90_
        self.f88 = f88
        self.f8 = f8
        self.f28 = f28
        self.f30 = f30
        self.f38 = f38
        self.f40 = f40
        self.f48 = f48
        self.f50 = f50
        self.f58 = f58
        self.f60 = f60
        self.f68 = f68
        self.f70 = f70
        self.f78 = f78
        self.f80 = f80

    def UporDown(self, signal):
        self.signal = signal
    
    def values(self):
        values = [self.v4_,self.f90_,self.f88,self.f8,self.f28,self.f30,self.f38,self.f40,self.f48,self.f50,self.f58,self.f60,self.f68,self.f70,self.f78,self.f80,self.signal]
        return(values)

def getRSX(source,prevRSX):
    length = 14
    f90_ = 0.0
    f88 = 0.0
    if (prevRSX.f90_ == 0.0):
        f90_ = 1.0
    elif (prevRSX.f88 <= prevRSX.f90_):
        f90_ = prevRSX.f88 + 1
    else:
        f90_ = prevRSX.f90_ + 1
    if ((prevRSX.f90_ == 0.0) and (length-1 >= 5)):
        f88 = length - 1.0
    else:
        f88 = 5.0
    f8 =  100.0*(source) 
    f18 = 3.0 / (length + 2.0) 
    f20 = 1.0 - f18 
    f10 = prevRSX.f8
    v8 = f8 - f10 
    f28 = f20 * prevRSX.f28 + f18 * v8 
    f30 = f18 * f28 + f20 * prevRSX.f30
    vC = f28 * 1.5 - f30 * 0.5 
    f38 = f20 * prevRSX.f38 + f18 * vC 
    f40 = f18 * f38 + f20 * prevRSX.f40
    v10 = f38 * 1.5 - f40 * 0.5 
    f48 = f20 * prevRSX.f48 + f18 * v10 
    f50 = f18 * f48 + f20 * prevRSX.f50
    v14 = f48 * 1.5 - f50 * 0.5 
    f58 = f20 * prevRSX.f58 + f18 * abs(v8) 
    f60 = f18 * f58 + f20 * prevRSX.f60
    v18 = f58 * 1.5 - f60 * 0.5
    f68 = f20 * prevRSX.f68 + f18 * v18 
    f70 = f18 * f68 + f20 * prevRSX.f70
    v1C = f68 * 1.5 - f70 * 0.5 
    f78 = f20 * prevRSX.f78 + f18 * v1C 
    f80 = f18 * f78 + f20 * prevRSX.f80
    v20 = f78 * 1.5 - f80 * 0.5
    f0 = 0.0
    if ((f88 >= f90_) and (f8 != f10)):
        f0 = 1.0
    else:
        f0 = 0.0
    f90 = 0.0
    if ((f88 == f90_) and (f0 == 0.0)):
        f90 = 0.0
    else:
        f90 = f90_
    v4_ = 0.0
    if ((f88 < f90) and (v20 > 0.0000000001)):
        v4_ = (v14 / v20 + 1.0) * 50.0
    else:
        v4_ = 50.0
    return(rsxValues(v4_,f90_,f88,f8,f28,f30,f38,f40,f48,f50,f58,f60,f68,f70,f78,f80))

class neuralValues():
    
    def __init__(self,l1_2,l2_1,l2_5,l2_9,l2_13,l2_17,l2_21,l2_25,l2_29,l2_32,l3_0):
        self.l1_2 =  l1_2
        self.l2_1 =  l2_1
        self.l2_5 =  l2_5
        self.l2_9 =  l2_9
        self.l2_13 = l2_13
        self.l2_17 = l2_17
        self.l2_21 = l2_21
        self.l2_25 = l2_25
        self.l2_29 = l2_29
        self.l2_32 = l2_32
        self.l3_0 =  l3_0

    def UporDown(self):
        return self.l3_0 > 0
    
    def values(self):
        values = [self.l3_0]
        return(values)
        
def getDiff(source, bigSource):
    delta = source - bigSource
    return (delta/bigSource)

def PineActivationFunctionTanh(v):
    return((exp(v) - exp(-v))/(exp(v) + exp(-v)))

def getNeural(source, bigSource):
    l0_0 = getDiff(source, bigSource)
    l1_0 = PineActivationFunctionTanh(l0_0*0.8446488687)
    l1_1 = PineActivationFunctionTanh(l0_0*-0.5674069006)
    l1_2 = PineActivationFunctionTanh(l0_0*0.8676766445)
    l1_3 = PineActivationFunctionTanh(l0_0*0.5200611473)
    l1_4 = PineActivationFunctionTanh(l0_0*-0.2215499554)
    l2_0 = PineActivationFunctionTanh(l1_0*0.3341657935 + l1_1*-2.0060003664 + l1_2*0.8606354375 + l1_3*0.9184846912 + l1_4*-0.8531172267)
    l2_1 = PineActivationFunctionTanh(l1_0*-0.0394076437 + l1_1*-0.4720374911 + l1_2*0.2900968524 + l1_3*1.0653326022 + l1_4*0.3000188806)
    l2_2 = PineActivationFunctionTanh(l1_0*-0.559307785 + l1_1*-0.9353655177 + l1_2*1.2133832962 + l1_3*0.1952686024 + l1_4*0.8552068166)
    l2_3 = PineActivationFunctionTanh(l1_0*-0.4293220754 + l1_1*0.8484259409 + l1_2*-0.7154087313 + l1_3*0.1102971055 + l1_4*0.2279392724)
    l2_4 = PineActivationFunctionTanh(l1_0*0.9111779155 + l1_1*0.2801691115 + l1_2*0.0039982713 + l1_3*-0.5648257117 + l1_4*0.3281705155)
    l2_5 = PineActivationFunctionTanh(l1_0*-0.2963954503 + l1_1*0.4046532178 + l1_2*0.2460580977 + l1_3*0.6608675819 + l1_4*-0.8732022547)
    l2_6 = PineActivationFunctionTanh(l1_0*0.8810811932 + l1_1*0.6903706878 + l1_2*-0.5953059103 + l1_3*-0.3084040686 + l1_4*-0.4038498853)
    l2_7 = PineActivationFunctionTanh(l1_0*-0.5687101164 + l1_1*0.2736758588 + l1_2*-0.2217360382 + l1_3*0.8742950972 + l1_4*0.2997583987)
    l2_8 = PineActivationFunctionTanh(l1_0*0.0708459913 + l1_1*0.8221730616 + l1_2*-0.7213265567 + l1_3*-0.3810462836 + l1_4*0.0503867753)
    l2_9 = PineActivationFunctionTanh(l1_0*0.4880140595 + l1_1*0.9466627196 + l1_2*1.0163097961 + l1_3*-0.9500386514 + l1_4*-0.6341709382)
    l2_10 = PineActivationFunctionTanh(l1_0*1.3402207103 + l1_1*0.0013395288 + l1_2*3.4813009133 + l1_3*-0.8636814677 + l1_4*41.3171047132)
    l2_11 = PineActivationFunctionTanh(l1_0*1.2388217292 + l1_1*-0.6520886912 + l1_2*0.3508321737 + l1_3*0.6640560714 + l1_4*1.5936220597)
    l2_12 = PineActivationFunctionTanh(l1_0*-0.1800525171 + l1_1*-0.2620989752 + l1_2*0.056675277 + l1_3*-0.5045395315 + l1_4*0.2732553554)
    l2_13 = PineActivationFunctionTanh(l1_0*-0.7776331454 + l1_1*0.1895231137 + l1_2*0.5384918862 + l1_3*0.093711904 + l1_4*-0.3725627758)
    l2_14 = PineActivationFunctionTanh(l1_0*-0.3181583022 + l1_1*0.2467979854 + l1_2*0.4341718676 + l1_3*-0.7277619935 + l1_4*0.1799381758)
    l2_15 = PineActivationFunctionTanh(l1_0*-0.5558227731 + l1_1*0.3666152536 + l1_2*0.1538243225 + l1_3*-0.8915928174 + l1_4*-0.7659355684)
    l2_16 = PineActivationFunctionTanh(l1_0*0.6111516061 + l1_1*-0.5459495224 + l1_2*-0.5724238425 + l1_3*-0.8553500765 + l1_4*-0.8696190472)
    l2_17 = PineActivationFunctionTanh(l1_0*0.6843667454 + l1_1*0.408652181 + l1_2*-0.8830470112 + l1_3*-0.8602324935 + l1_4*0.1135462621)
    l2_18 = PineActivationFunctionTanh(l1_0*-0.1569048216 + l1_1*-1.4643247888 + l1_2*0.5557152813 + l1_3*1.0482791924 + l1_4*1.4523116833)
    l2_19 = PineActivationFunctionTanh(l1_0*0.5207514017 + l1_1*-0.2734444192 + l1_2*-0.3328660936 + l1_3*-0.7941515963 + l1_4*-0.3536051491)
    l2_20 = PineActivationFunctionTanh(l1_0*-0.4097807954 + l1_1*0.3198619826 + l1_2*0.461681627 + l1_3*-0.1135575498 + l1_4*0.7103339851)
    l2_21 = PineActivationFunctionTanh(l1_0*-0.8725014237 + l1_1*-1.0312091401 + l1_2*0.2267643037 + l1_3*-0.6814258121 + l1_4*0.7524828703)
    l2_22 = PineActivationFunctionTanh(l1_0*-0.3986855003 + l1_1*0.4962556631 + l1_2*-0.7330224516 + l1_3*0.7355772164 + l1_4*0.3180141739)
    l2_23 = PineActivationFunctionTanh(l1_0*-1.083080442 + l1_1*1.8752543187 + l1_2*0.3623326265 + l1_3*-0.348145191 + l1_4*0.1977935038)
    l2_24 = PineActivationFunctionTanh(l1_0*-0.0291290625 + l1_1*0.0612906199 + l1_2*0.1219696687 + l1_3*-1.0273685429 + l1_4*0.0872219768)
    l2_25 = PineActivationFunctionTanh(l1_0*0.931791094 + l1_1*-0.313753684 + l1_2*-0.3028724837 + l1_3*0.7387076712 + l1_4*0.3806140391)
    l2_26 = PineActivationFunctionTanh(l1_0*0.2630619402 + l1_1*-1.9827996702 + l1_2*-0.7741413496 + l1_3*0.1262957444 + l1_4*0.2248777886)
    l2_27 = PineActivationFunctionTanh(l1_0*-0.2666322362 + l1_1*-1.124654664 + l1_2*0.7288282621 + l1_3*-0.1384289204 + l1_4*0.2395966188)
    l2_28 = PineActivationFunctionTanh(l1_0*0.6611845175 + l1_1*0.0466048937 + l1_2*-0.1980999993 + l1_3*0.8152350927 + l1_4*0.0032723211)
    l2_29 = PineActivationFunctionTanh(l1_0*-0.3150344751 + l1_1*0.1391754608 + l1_2*0.5462816249 + l1_3*-0.7952302364 + l1_4*-0.7520712378)
    l2_30 = PineActivationFunctionTanh(l1_0*-0.0576916066 + l1_1*0.3678415302 + l1_2*0.6802537378 + l1_3*1.1437036331 + l1_4*-0.8637405666)
    l2_31 = PineActivationFunctionTanh(l1_0*0.7016273068 + l1_1*0.3978601709 + l1_2*0.3157049654 + l1_3*-0.2528455662 + l1_4*-0.8614146703)
    l2_32 = PineActivationFunctionTanh(l1_0*1.1741126834 + l1_1*-1.4046408959 + l1_2*1.2914477803 + l1_3*0.9904052964 + l1_4*-0.6980155826)
    l3_0 = PineActivationFunctionTanh(l2_0*-0.1366382003 + l2_1*0.8161960822 + l2_2*-0.9458773183 + l2_3*0.4692969576 + l2_4*0.0126710629 + l2_5*-0.0403001012 + l2_6*-0.0116244898 + l2_7*-0.4874816289 + l2_8*-0.6392241448 + l2_9*-0.410338398 + l2_10*-0.1181027081 + l2_11*0.1075562037 + l2_12*-0.5948728252 + l2_13*0.5593677345 + l2_14*-0.3642935247 + l2_15*-0.2867603217 + l2_16*0.142250271 + l2_17*-0.0535698019 + l2_18*-0.034007685 + l2_19*-0.3594532426 + l2_20*0.2551095195 + l2_21*0.4214344983 + l2_22*0.8941621336 + l2_23*0.6283377368 + l2_24*-0.7138020667 + l2_25*-0.1426738249 + l2_26*0.172671223 + l2_27*0.0714824385 + l2_28*-0.3268182144 + l2_29*-0.0078989755 + l2_30*-0.2032828145 + l2_31*-0.0260631534 + l2_32*0.4918037012)
    return(neuralValues(l1_2,l2_1,l2_5,l2_9,l2_13,l2_17,l2_21,l2_25,l2_29,l2_32,l3_0))

class fxData():

    def __init__(self,time,open_,high,low,close):
        self.time = time
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.ohlc = (open_+high+low+close)/4
        self.change = open_-close

    def setRSX(self,rsxValues):
        self.rsxValues = rsxValues
    
    def setBigSource(self, bigSource):
        self.bigSource = bigSource

    def setNeural(self, neurals):
        self.neurals = neurals

    def setY(self, y):
        self.y = y

    def values(self):
        list0 = [self.time, self.open, self.high, self.low, self.close, self.ohlc, self.change, self.bigSource]
        list1 = self.rsxValues.values()
        list2 = self.neurals.values()
        list3 = [self.neurals.UporDown(), self.y]
        return(list0 + list1 + list2 + list3)

def saveData(candleData):
    with open(outputFile, 'a', newline='') as data_file:
        entryWrite = csv.writer(data_file)
        entryWrite.writerow(candleData.values())

def getMinute(rawTime):
    return float(rawTime.split(':')[1])%5

currentData = []
def processCurrentCandle(candle):
    if(getMinute(candle.time) == 0):
        if(len(currentData) > 0):
            o_ = currentData[0].open
            h_ = 0
            l_ = 0
            c_ = currentData[len(currentData)-1].close
            for i in currentData:
                if i.high > h_:
                    h_ = i.high
                if (i.low < l_ or l_==0):
                    l_ = i.low
            candle.setBigSource((o_+h_+l_+c_)/4)
        else:
            candle.setBigSource(candle.ohlc)
    else:
        if(len(currentData) > 0):
            candle.setBigSource(currentData[len(currentData)-1].ohlc)
        else:
            candle.setBigSource(candle.ohlc)
    
    candle.setNeural(getNeural(candle.ohlc,candle.bigSource))

    rsx = None
    if(len(currentData)>0):
        rsx = getRSX(candle.ohlc,currentData[len(currentData)-1].rsxValues)
        if(rsx.v4_ > currentData[len(currentData)-1].rsxValues.v4_):
            rsx.UporDown(True)
        else:
            rsx.UporDown(False)
    else:
        rsx = getRSX(candle.ohlc,rsxValues(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        rsx.UporDown(False)
    candle.setRSX(rsx)

    if(len(currentData)==6):
        result = currentData[1]
        openValue = result.open
        closeValue = candle.close
        y = 0
        if closeValue>openValue:
            y = 1
        elif closeValue<openValue:
            y = 0
        result.setY(y)

        # if(result.neurals.UporDown() != currentData[0].neurals.UporDown()):
        saveData(result)

        currentData.remove(currentData[0])

    currentData.append(candle)

def processData():
    print(time.time())
    with open(inputFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = fxData(row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]))
            processCurrentCandle(data)
    print('time:',time.time())

with open(outputFile, 'a', newline='') as data_file:
    entryWrite = csv.writer(data_file)
    entryWrite.writerow(['time', 'open', 'high', 'low', 'close', 'ohlc', 'change','big_source', 'v4_', 'f90_', 'f88', 'f8','f28','f30','f38','f40','f48','f50','f58','f60','f68','f70','f78','f80','signalRSX','l3_0','signalN', 'y'])

processData()



