#include "branch.h"
#include <algorithm>
#include <vector>
#include "team.h"

Branch::Branch(std::vector<Team>& teams, double probability) : teams(teams), probability(probability) {
};

/**
	Compare team1 team with team2.  Returns true if the team represented by the team1
	is ranked higher (i.e., ranked 1st vs. ranked 40th), false if this team is ranked
	lower (i.e., ranked 40th vs. ranked 1st), and false if they are ranked identically.
*/

bool Branch::compare(Team & team1, Team & team2){
	if(team1.getFirstSort() > team2.getFirstSort()){
		return true;
	}else if(team1.getFirstSort() < team2.getFirstSort()){
		return false;
	}else{
		if(team1.getSecondSort() > team2.getSecondSort()){
			return true;
		}else if(team1.getSecondSort() < team2.getSecondSort()){
			return false;
		}else{
			if(team1.getThirdSort() > team2.getThirdSort()){
				return true;
			}else if(team1.getThirdSort() < team2.getThirdSort()){
				return false;
			}else{
				if(team1.getFourthSort() > team2.getFourthSort()){
					return true;
				}else if(team1.getFourthSort() < team2.getFourthSort()){
					return false;
				}else{
					if(team1.getFifthSort() > team2.getFifthSort()){
						return true;
					}else if(team1.getFifthSort() < team2.getFifthSort()){
						return false;
					}else{
						return false;
					}
				}
			}
		}
	}
}

void Branch::sort(){
	//std::sort()
}

double Branch::getProbability(){
	return probability;
}

Team* Branch::findTeam(int teamNumber){
	for (int i = 0; i < teams.size(); i++) {
		if(teams[i].getTeamNumber() == teamNumber){
			return &teams[i];
		}
	}
	//return null_ptr;
}

int main(){
	std::vector<Team> teams;
	teams.push_back(Team(20, 1, 1, 1, 1, 1));
	teams.push_back(Team(469, 2, 2, 2, 2, 2));
	teams.push_back(Team(1114, 3, 3, 3, 3, 3));
	Branch branch;
	branch = Branch(&teams, .5);
	return 0;
}
