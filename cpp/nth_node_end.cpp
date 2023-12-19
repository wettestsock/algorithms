#include <iostream>

/*
REMOVE NTH NODE BACKWARDS FROM FOTWARD LINKED LIST

clang++ nth_node_end.cpp -o linout/n_th_node_end

*/



struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head->next && n == 1){
            delete head;
            return NULL;
        }

        //will be the node BEFORE the to-be-removed node
        ListNode* c = new ListNode(-1, head);
        

        while(c){
            //amount of nodes in front of current
            int ahead_num = 0;

            
            ListNode* ahead = c->next;
            while(ahead) {
                ahead_num++;
                ahead = ahead->next;
            }

            if(ahead_num == n){
                //if need to delete head
                if(c->val == -1){
                    head = c->next->next;
                    delete c->next;
                    delete c;
                    
                } else {
                    ListNode* temp = c->next;
                    c->next = c->next->next;
                    delete temp;
                }
                return head;
            }

            c=c->next;
        }
        

        


        


        return head;

    }
};

int main(){
    return 0;
}