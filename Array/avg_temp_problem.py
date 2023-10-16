import array
def calculate_average(array_to_calculate_average: array) -> float:
    return sum(array_to_calculate_average)/len(array_to_calculate_average)

def count_days_whose_temp_is_above_given_temp(array_to_traverse: array, temperature: float):
    day_count = 0
    for item in array_to_traverse:
        if item > temperature:
            day_count = day_count + 1
    return day_count

def main():
    days_count = int(input('How many days data you want to record :'))
    input_array = array.array('f',[])

    temp_flag = 0
    while temp_flag < days_count:
        input_array.append(float(input(f"Enter {temp_flag+1} day's temperature : ")))
        temp_flag = temp_flag + 1
    
    average = calculate_average(array_to_calculate_average=input_array)
    days_above_avg_temp = count_days_whose_temp_is_above_given_temp(array_to_traverse=input_array,temperature=average)
    print(f"Average temperature is : {average}")
    print(f"Days Count with above Average temperature is : {days_above_avg_temp}")
    
    
    

main()
    
        
        