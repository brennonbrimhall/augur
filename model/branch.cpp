#include "branch.h"
#include <algorithm>


/**
	Compare team1 team with team2.  Returns true if the team represented by the team1
	is ranked higher (i.e., ranked 1st vs. ranked 40th), false if this team is ranked
	lower (i.e., ranked 40th vs. ranked 1st), and false if they are ranked identically.
*/

bool Branch::compare(Team const & team1, Team const & team2){
	if(team1.getFirstSort() > team.getFirstSort()){
		return true;
	}else if(team1.getFirstSort() < team.getFirstSort()){
		return false;
	}else{
		if(team1.getSecondSort() > team.getSecondSort()){
			return true;
		}else if(team1.getSecondSort() < team.getSecondSort()){
			return false;
		}else{
			if(team1.getThirdSort() > team.getThirdSort()){
				return true;
			}else if(team1.getThirdSort() < team.getThirdSort()){
				return false;
			}else{
				if(team1.getFourthSort() > team.getFourthSort()){
					return true;
				}else if(team1.getFourthSort() < team.getFourthSort()){
					return false;
				}else{
					if(team1.getFifthSort() > team.getFifthSort()){
						return true;
					}else if(team1.getFifthSort() < team.getFifthSort(){
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
	std::sort()
}