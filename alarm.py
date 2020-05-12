import time
import winsound

def alarm():

    try:
        mytime = list(map(int, input('Digite o horário: ').split()))
        if len(mytime) == 3:
            total_seconds=mytime[0]*60*60+mytime[1]*60+mytime[2]
            time.sleep(total_seconds)
            frequency = 2500
            duration = 1000
            winsound.Beep(frequency, duration)

        else:
            print('Por favor, digite o tempo no formato correto')
            alarm()

    except Exception as e:
        print('Isto é uma exceção.',e,'Então, por favor, coloque os detalhes correntamente')
        alarm()
alarm()