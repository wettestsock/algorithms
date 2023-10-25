#include <iostream>
#include <vector>

/*
GENERATE PARENTHESIS

generate every combination of such 

g++ genparentheses.cpp -o out\genparentheses
out\genparentheses

g++ genparentheses.cpp -o linout/genparentheses
linout/genparentheses

*/


void recurs(int openN, int closeN, std::string temp, std::vector<std::string>& out) {
    if (!openN && !closeN) out.push_back(temp);

    if (openN > 0) recurs(openN - 1, closeN, temp.append("("), out);
    if (openN < closeN) recurs(openN, closeN - 1, temp.append(")"), out);
};

std::vector<std::string> generateParenthesis(const int& n) {
    std::vector<std::string> output;



    recurs(n, n, "", output);
    return output;
}

std::ostream& operator<<(std::ostream& out, const std::vector<std::string>& input) {
    int i = 0;
    out << '{';
    while (i < input.size() - 1) {
        out << input[i] << ", ";
        i++;
    }
    out << input[i] << "}\n";
    return out;

};





int main() {
    std::cout << generateParenthesis(3);


}