print('Hvor mange er dere på laget?')
lag = int(input())

print('Hvor mange twist er det i posen dere vant?')
antall_twist = int(input())

twist_lag = antall_twist // lag
rest_twist = antall_twist - twist_lag * lag

print(f'Det blir {twist_lag} twist til hver, og det blir {rest_twist} twist til overs.')