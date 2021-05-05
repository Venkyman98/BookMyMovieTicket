class BookmySeat:

    def __init__(self):
        print()
        print('Welcome to IMAX!')
        print()
        print('Please enter the number of rows:')
        self.row = int(input())
        print('Please enter the number of seats:')
        self.seat = int(input())
        self.total_seats = self.row*self.seat
        self.seating = []
        self.user_info = [[None for j in range(self.seat)] for i in range(self.row)]
        self.ticketspurchased = 0
        self.current_income = 0

        for i in range(self.row):                          
            a = []
            for j in range(self.seat):
                a.append('S')
            self.seating.append(a)
        print(end='  ')
        self.menu()
     

    def show_seats(self):           
        print('Here are the seats:\n')
        count1,count2 = 0,0
        print(end='  ')
        for j in range(1, self.seat + 1):        
            count1 = count1 + 1
            print(count1, end=' ')
        print()
        for i in self.seating:
            count2 = count2 + 1
            print(count2, end=" ")
            print(' '.join(i), sep=',')
    
    def buy(self):
        self.buy_row = int(input('Enter the Row you want:'))
        print()
        self.buy_seat=int(input('Enter the seat you want in the selected row:'))        
        print()
        if self.seating[self.buy_row-1][self.buy_seat-1] == 'S':
            print('Cost of the seat chosen is:',self.ticketprice(self.buy_row))
            print()
            user_input = input('Type yes for confirming your ticket and no to Stop your booking: ')
            user_info_dict = {}
            if (user_input == 'Yes' or user_input == 'yes'):
                user_info_dict['Name'] = input('Enter your name: ')
                user_info_dict['Gender'] = input('Gender: ')
                user_info_dict['Age'] = input('Enter Age: ')
                user_info_dict['Contact_number'] = input('Enter your Contact Number: ')
                print()
                self.seating[self.buy_row-1][self.buy_seat-1] = 'B'
                self.ticketspurchased += 1
                self.current_income += self.ticketprice(self.buy_row)
            else:
                self.menu()
            self.user_info[self.buy_row-1][self.buy_seat-1] = user_info_dict
            print('Your Ticket has been booked successfully! Have fun!')
            print()
        else:
            print('This seat has already been booked!')
            print()

    def ticketprice(self,a):
        if self.total_seats<=60:
            self.price=10
        else:
            if a<=(self.row//2):
                self.price=10
            else:
                self.price=8
        return self.price

    def statistics(self):
        self.total_income = 0
        for i in range(1,self.row+1):
            self.total_income += self.ticketprice(i)*self.seat
        percentage = (self.current_income/self.total_income)*100

        print('Number of Tickets purchased: ',self.ticketspurchased)
        print('Percentage',percentage)
        print('Current income:',self.current_income)
        print('Total income:',self.total_income)
        print()


    def seat_info(self):
        a=int(input("Enter your Row number: "))
        b=int(input("Enter your Seat number: "))
        print()
        if self.seating[a-1][b-1] == 'B':
            x = self.user_info[a-1][b-1]
            print('Name: ',x['Name'])
            print('Gender: ',x['Gender'])
            print('Age: ',x['Age'])
            print('Contact number: ',x['Contact_number'])
            print()
        else:
            print('Seat is empty')


    def menu(self):     
        print('\n1] Show Seats: \n2] Buy a ticket: \n3] Show Statistics: \n4] Details of Booked users:\nPress 0 to exit')
        print()
        choice=int(input())
        if choice==1:
            self.show_seats()
            self.menu()
        elif choice==2:
            self.buy()
            self.menu()
        elif choice==3:
        	self.statistics()
        	self.menu()
        elif choice==4:
        	self.seat_info()
        	self.menu()
        else:
            print('Have a nice day :)')



Movie = BookmySeat()
    
