#include <iostream>
using namespace std;

class accountInfo{
    public:
    double Balance;
    double BalanceI;
    int deposits;
    int withdrawls;
    double intrest;
    double service_charge;
    accountInfo(){
        Balance = 0;
        BalanceI = 0;
        intrest = 0;
        deposits = 0;
        withdrawls = 0;
        service_charge = 0;
    }
    accountInfo(double B, double I){
        Balance = B;
        intrest = I;
    }
    virtual void deposit(double d){
        Balance = Balance + d;
        if (deposits == 0){
            BalanceI = Balance;
        }
        deposits += 1;

    }
    virtual void withdrawl(double W){
        Balance = Balance - W;
        withdrawls += 1;

    }
    virtual void calcInt(){
        double MIR = intrest /12;
        double MI = Balance * MIR;
        Balance = Balance + abs(MI);
    }
    virtual void monthlyProc(){
        Balance = Balance - service_charge;
        calcInt();
        withdrawls = 0;
        deposits = 0;
        BalanceI = Balance;
    }

};
class saving : public accountInfo{
public:
bool status;
saving(double x, double y)
{   Balance = x;
    intrest = y;
    if ( Balance < 25){
        status = false;
    }else{
        status = true ;
    }}
void withdrawl(double W){
    if ( Balance < 25){
        status = false;
    }else{
        status = true ;
    }
    if (status == true){
        accountInfo::withdrawl(W);
    }else{
        cout<<"Your account is Inactive"<<endl;
    }
}
void deposit(double d){
    if( Balance + d >25 ){
        accountInfo::deposit(d);
        status = true;
    }else{
        accountInfo::deposit(d);
        status = false;
    }
}
void monthlyProc(){
    if ( withdrawls > 4){
        service_charge = withdrawls - 4;
        accountInfo::monthlyProc();
    }else{
        service_charge = 0;
        accountInfo::monthlyProc();
    }
    if ( Balance < 25){
        status = false;
    }else{
        status = true ;
    }
}
};

class checking : public accountInfo{
    public:
    checking(double x, double y){
        Balance = x;
        intrest = y;
    }
    void withdrawl(double w){
        if (Balance - w < 0 ){
            cout<< "Not Enough Balance, withdraw not possible, service charge of 15 will be provided instead"<<endl;
            service_charge += 15;
        }else{
            accountInfo::withdrawl(w);
        }
    }
    void monthlyProc(){
        service_charge = 5;
        service_charge = service_charge + withdrawls*0.1;
        accountInfo::monthlyProc();
    }

    void deposit(double d){
        accountInfo::deposit(d);

    }
};
int main(){
    saving S(0.0,1.2);
    checking C(0.0,1.2);
    int choice;
    while(choice != 7){
        cout<< "Bank account menu: "<< endl
            << "1. Saving account deposits"<< endl
            << "2. Saving account withdraws"<<endl
            << "3. Checking account deposits"<<endl
            << "4. Checking account withdraws"<< endl
            << "5. Monthly statistics calculation"<< endl
            << "6. statistics print"<< endl
            << "7. Exit"<<endl;
            cin >> choice;
        switch (choice){
            case 1:
                double d;
                cout << "Enter Amount to be deposited"<<endl;
                cin>> d;
                S.deposit(d); 
                break;
            case 2:
                double w;
                cout << "Enter Amount to be withdrawn"<<endl;
                cin>> w;
                S.withdrawl(w); 
                break;
            case 3:
                double d1;
                cout << "Enter Amount to be deposited"<<endl;
                cin>> d1;
                C.deposit(d1); 
                break;
            case 4:
                double w1;
                cout << "Enter Amount to be withdrawn"<<endl;
                cin>> w1;
                C.withdrawl(w1); 
                break;
            case 5:
                S.monthlyProc();
                C.monthlyProc();
                break;
            case 6:
                cout<<"Saving Account Info: "<< endl
                    << "Starting balance: "<< S.BalanceI<< endl
                    << "Ending balance: "<< S.Balance<< endl
                    << "Number of Withdrawals: "<< S.withdrawls << endl
                    << "Number of Deposits: "<< S.deposits << endl
                    << "Service Charge : "<< S.service_charge << endl
                    <<"\n"
                    << "Checking Account Info: "<< endl
                    << "Starting balance: "<< C.BalanceI<< endl
                    << "Ending balance: "<< C.Balance<< endl
                    << "Number of Withdrawals: "<< C.withdrawls << endl
                    << "Number of Deposits: "<< C.deposits << endl
                    << "Service Charge : "<< C.service_charge << endl;
                    
                break;
            case 7:
            break;
            default:
                cout<<"Invalid Entry"<<endl;
            
        }
    }
}