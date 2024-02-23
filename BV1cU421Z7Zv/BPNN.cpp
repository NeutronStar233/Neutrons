#include "BPNN.h"
#include <iostream>

BPNN::BPNN()
{
	m_activity_function = RELU;
	m_d_activity_function = D_RELU;
}
BPNN::BPNN(int firstLayerNeuronsNumber,function<float(float)> af, function<float(float)> Daf)
{
	this->m_layers.push_back(vector<float>());
	for (int i = 0; i < firstLayerNeuronsNumber; i++)
	{
		this->m_layers[0].push_back(0);
	}
	m_activity_function = af;
	m_d_activity_function = Daf;
}

void BPNN::AddLayer(int layerNeuronNumber)
{
	this->m_layers.push_back(vector<float>());
	for (int i = 0; i < layerNeuronNumber; i++)
	{
		m_layers[m_layers.size() - 1].push_back(0);
	}
	this->m_bias.push_back(vector<float>());
	for (int i = 0; i < layerNeuronNumber; i++)
	{
		m_bias[m_bias.size()-1].push_back(RANDOMNUMBER);
	}
	this->m_weights.push_back(vector<vector<float>/*j*/ >/*i*/());
	for (int i = 0; i < m_layers[this->m_layers.size() - 2].size(); i++)
	{
		m_weights[m_weights.size()-1].push_back(vector<float>());
		for (int j = 0; j < layerNeuronNumber; j++)
		{
			m_weights[m_weights.size() - 1][m_weights[m_weights.size() - 1].size() - 1].push_back(RANDOMNUMBER);
		}
	}
}

void BPNN::Forward()
{
	for (int layer = 1; layer < this->m_layers.size(); layer++)
	{
		for (int j = 0; j < m_layers[layer].size(); j++)
		{
			float sum = 0;
			for (int i = 0; i < m_layers[layer - 1].size(); i++)
			{
				sum += m_weights[layer - 1][i][j] * m_layers[layer - 1][i];
			}
			sum += m_bias[layer - 1][j];
			sum = m_activity_function(sum);
			m_layers[layer][j] = sum;
		}
	}
}

void BPNN::Train(float Delta, float r)
{
	float C = 0;
	for (int j = 0; j < this->m_target.size(); j++)
	{
		C += pow(this->m_layers[m_layers.size() - 1][j] - m_target[j], 2);
	}
	C = C / 2;
	while (C > Delta)
	{
		auto DLayers = m_layers;
		auto DBias = m_bias;
		auto DWeights = m_weights;

		for (int j = 0; j < DLayers[DLayers.size() - 1].size(); j++)
		{
			DLayers[DLayers.size() - 1][j] = m_layers[m_layers.size() - 1][j] - m_target[j];
		}

		for (int layer = m_layers.size() - 1; layer > 0; layer--)
		{
			if (layer != m_layers.size() - 1)
			{
				for (int j = 0; j < DLayers[layer].size(); j++)
				{
					float sum = 0;
					for (int k = 0; k < m_layers[layer + 1].size(); k++)
					{
						float DCAK = DLayers[layer+1][k];
						float sumJ = 0;
						for (int J = 0; J < DLayers[layer].size(); J++)
						{
							sumJ += m_weights[layer][J][k] * m_layers[layer][J];
						}
						sumJ += m_bias[layer][k];
						sumJ = m_activity_function(sumJ);
						sumJ *= m_weights[layer][j][k];
						sum += DCAK * sumJ;
					}
					DLayers[layer][j] = sum;
				}
			}
			for (int j = 0; j < m_layers[layer].size(); j++)
			{
				float K = 0;
				for (int i = 0; i < m_layers[layer - 1].size(); i++)
				{
					K += m_weights[layer - 1][i][j] * m_layers[layer - 1][i];
				}
				K += m_bias[layer - 1][j];
				K = m_d_activity_function(K);

				DBias[layer-1][j] = DLayers[layer][j]*K;
				for (int i = 0; i < m_layers[layer - 1].size(); i++)
				{
					DWeights[layer - 1][i][j] = DLayers[layer][j]*K * m_layers[layer - 1][i];
				}
			}
		}

		for (int layer = 1; layer < m_layers.size(); layer++)
		{
			for (int j = 0; j < m_layers[layer].size(); j++)
			{
				m_bias[layer - 1][j] -= r * DBias[layer - 1][j];
				for (int i = 0; i < m_layers[layer - 1].size(); i++)
				{
					m_weights[layer - 1][i][j] -= r * DWeights[layer - 1][i][j];
				}
			}
		}
		Forward();

		C = 0;
		for (int j = 0; j < this->m_target.size(); j++)
		{
			C += pow(this->m_layers[m_layers.size() - 1][j] - m_target[j], 2);
		}
		C = C / 2;
		cout << "C: " << C << endl;
	}
}