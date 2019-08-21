def mean(num_list):
        
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError as detail:
        msg = "Please provide a list"
        raise TypeError(detail.__str__()+"\n" + msg)

#        msg ="Why you trying to divide by 0?? Provide a better list."
#       raise ZeroDivisionError(detail.__str__()+"\n" +msg)
 
