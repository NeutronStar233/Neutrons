#include<iostream>
#include<string>
#include"BPNN.h"

using namespace std;

#define INPUT 1
#define OUTPUT 1

int main()
{
	BPNN bp(INPUT);
	bp.AddLayer(2);
	bp.AddLayer(OUTPUT);

	string command;
	while (true)
	{
		cin >> command;
		if (command == "i=")
		{
			for (int i = 0; i < INPUT; i++)
			{
				cin >> bp.m_layers[0][i];
			}
		}
		else if (command == "check")
		{
			for (int layer = 1; layer < bp.m_layers.size(); layer++)
			{
				cout << "Layer: " << layer << endl;
				cout << "Neurons: " << endl;
				for (int j = 0; j < bp.m_layers[layer].size(); j++)
				{
					cout << "a_" << j << ": " << bp.m_layers[layer][j] << endl;
				}
				cout << "Bias:" << endl;
				for (int j = 0; j < bp.m_bias[layer - 1].size(); j++)
				{
					cout << "b_" << j << ": " << bp.m_bias[layer - 1][j] << endl;
				}
				cout << "Weights£» "<<endl;
				for (int i = 0; i < bp.m_weights[layer - 1].size(); i++)
				{
					for (int j = 0; j < bp.m_weights[layer - 1][i].size(); j++)
					{
						cout << "W_" << i << "," << j << ": " << bp.m_weights[layer - 1][i][j] << "    ";
					}
					cout << endl;
				}
			}
		}
		else if (command == "test")
		{
			bp.Forward();
			for (int j = 0; j < bp.m_layers[bp.m_layers.size()-1].size(); j++)
			{
				cout << "a_" << j << ": " << bp.m_layers[bp.m_layers.size() - 1][j] << endl;
			}
		}
		else if (command == "t=")
		{
			vector<float> v;
			float a;
			for (int i = 0; i < OUTPUT; i++)
			{
				cin >> a;
				v.push_back(a);
			}
			bp.m_target = v;
		}
		else if (command == "train")
		{
			float Delta, r;
			cin >> Delta >> r;
			bp.Train(Delta,r);
			bp.Forward();
			for (int j = 0; j < bp.m_layers[bp.m_layers.size() - 1].size(); j++)
			{
				cout << "a_" << j << ": " << bp.m_layers[bp.m_layers.size() - 1][j] << endl;
			}
		}
		else
		{
			cout << "WTF ARE YOU TYPING" << endl;
		}
	}

	system("pause");
	return 0;
}