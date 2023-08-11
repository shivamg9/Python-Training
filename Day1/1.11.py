# Write a program a function for ATM machine which takes amount as input and output should be number of notes of each denomination. 
# The ATM has notes in following denomination : 2000, 500, 100.
# Note that the ATM machine rarely gives all notes of a single amount. 
# If you enter 4000, it will give 1 2000rs, 3 500rs and 5 100rs	notes for even distribution.sls

def atm(amnt):
    note2000 = note500 = note100 = 0
    if amnt% 2000==0:
        note2000 = amnt // 2000-1
        amnt = amnt - note2000 * 2000
        
    if amnt%500==0:
        note500 = amnt // 500-1
        amnt = amnt - note500 * 500
    if amnt%100==0:
        note100 = amnt // 100
        amnt = amnt - note100 * 100
    print(f"2000: {note2000}")
    print(f"500: {note500}")
    print(f"100: {note100}")

amount=int(input("enter a amount : "))
print(atm(amount))

