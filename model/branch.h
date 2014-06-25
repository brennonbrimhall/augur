#ifndef Branch_H
#define Branch_H

#include <vector>
#include "team.h"

class Branch {
	private:
		double probability;
		std::vector<Team> teams;
	public:
		Branch(std::vector<Team>& teams, double probability);
		void sort();
		bool compare(Team & team1, Team & team2);
		double getProbability();
		Team* findTeam(int teamNumber);
};
#endif
