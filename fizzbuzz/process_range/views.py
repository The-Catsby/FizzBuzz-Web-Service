from django.http import HttpResponse

def fizzy(request):
    begin = int(request.GET.get('begin', 1))
    end   = int(request.GET.get('end', 0))
    response = ''

    for number in range(begin, end+1):
        if (number % 3) == 0 and (number % 5) == 0:
            response += 'FizzBuzz'
        elif (number % 3) == 0:
            response += 'Fizz'
        elif (number % 5) == 0:
            response += 'Buzz'
        else:
            response += str(number)

        response += ' \n'

    return HttpResponse(response)
