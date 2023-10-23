#include <iostream>
#include <memory>

/*
ADD 2 NUMBERS IN CPP

for further documentation, look at the .py file


g++ add2nums.cpp -o out/add2nums
out/add2nums
*/

struct node{
    int val;
    node* next;
    
    //member initialization lists
    node(): val(0), next(nullptr) {} //empty vals
    node(int x): val(x), next(nullptr) {} //just int
    node(int x, node *next): val(x), next(next) {} //int and next ptr
        
    void deallocate();
    void insert_end(int x);
};

void node::insert_end(int x) {
        node* new_node = new node(x);
        new_node->val = x;
        new_node->next = nullptr;

        node* c = this;
        while (c->next) c = c->next;
        c->next = new_node;

    }

void node::deallocate(){
    node* c = this;
    while(c) {
        std::cout<<"freed node val " << c->val << '\n';
        node* temp = c;
        c=c->next;
        delete temp;

    }
};

std::ostream& operator<<(std::ostream& out, node* head) {
    node* c = head;
        while (c->next) {
            out<< c->val << " <- ";
            c = c->next;
        };
    out<<c->val << '\n';
    return out;
}

class solution {
    public:
    node* add_two_nums(node* l1, node* l2) {
        node* temp = new node(); // for forward leftover edge cases

        node* c = temp;
        int carry = 0;

        while(l1 || l2 || carry) {
            int val1 = l1? l1->val : 0;
            int val2 = l2? l2->val : 0;

            //new digit
            int new_val = val1+val2+carry;
            carry = (int)(new_val/10); //gets the tenth place, 0 if under 10
            new_val %= 10;  //gets the ones place of num

            c->next = new node(new_val); //new node for the output
            c= c->next; //iterates to the next node in the output

            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;



        }

        return temp->next;
    }
};

int main() {
    node* a1 = new node(3);
    a1->insert_end(5);
    a1->insert_end(2);

    node* b1 = new node(5);
    b1->insert_end(5);
    b1->insert_end(7);

    std::cout<<a1 << b1 << solution::add_two_nums(a1,b1);
    a1->deallocate();
    b1->deallocate();
    a1 = nullptr;
    b1 = nullptr;



    //std::cin.get();
}
