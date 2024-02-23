#pragma once
#include<vector>
#include<functional>
#include<cstdlib>
using namespace std;

#define RELU [](float x){if(x > 0){return x;}else{return float(0);}}
#define D_RELU [](float x){if(x > 0){return float(1);}else{return float(0);}}

#define RANDOMNUMBER float(rand()%100)/100

class BPNN
{
public:
	BPNN();
	BPNN(int firstLayerNeuronsNumber, function<float(float)> af = RELU, function<float(float)> Daf = D_RELU);

	void AddLayer(int layerNeuronNumber);

	void Forward();

	void Train(float Delta,float r);

	function<float(float)> m_activity_function;
	function<float(float)> m_d_activity_function;

	vector<vector<float> > m_layers;
	vector<vector<float> > m_bias;
	vector<vector<vector<float>/*j*/ >/*i*/ > m_weights;//[layer][i][j]
	vector<float> m_target;
};

