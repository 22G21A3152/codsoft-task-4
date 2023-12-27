{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "cLRO431gs-Nd"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv(\"advertising.csv\")"
      ],
      "metadata": {
        "id": "YyUodutstxpf"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "EZsb9O4MviaI",
        "outputId": "adc33e95-2ea8-4057-cad2-9c25c6636465"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      TV  Radio  Newspaper  Sales\n",
              "0  230.1   37.8       69.2   22.1\n",
              "1   44.5   39.3       45.1   10.4\n",
              "2   17.2   45.9       69.3   12.0\n",
              "3  151.5   41.3       58.5   16.5\n",
              "4  180.8   10.8       58.4   17.9"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-20f93d72-3cf6-41ef-8c5a-a9333fe1b42a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>TV</th>\n",
              "      <th>Radio</th>\n",
              "      <th>Newspaper</th>\n",
              "      <th>Sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>230.1</td>\n",
              "      <td>37.8</td>\n",
              "      <td>69.2</td>\n",
              "      <td>22.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>44.5</td>\n",
              "      <td>39.3</td>\n",
              "      <td>45.1</td>\n",
              "      <td>10.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>17.2</td>\n",
              "      <td>45.9</td>\n",
              "      <td>69.3</td>\n",
              "      <td>12.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>151.5</td>\n",
              "      <td>41.3</td>\n",
              "      <td>58.5</td>\n",
              "      <td>16.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>180.8</td>\n",
              "      <td>10.8</td>\n",
              "      <td>58.4</td>\n",
              "      <td>17.9</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-20f93d72-3cf6-41ef-8c5a-a9333fe1b42a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-20f93d72-3cf6-41ef-8c5a-a9333fe1b42a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-20f93d72-3cf6-41ef-8c5a-a9333fe1b42a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-666e9b8f-f517-43fd-a9e4-f43221fc85db\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-666e9b8f-f517-43fd-a9e4-f43221fc85db')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-666e9b8f-f517-43fd-a9e4-f43221fc85db button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OW1N3Slnvl6B",
        "outputId": "b22785c4-f65c-45e7-8db1-f2eed1b4dbbf"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(200, 4)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "kjKr_Y_Qvpp_",
        "outputId": "baaa9bff-341a-43a8-f08f-4b5ab1362867"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               TV       Radio   Newspaper       Sales\n",
              "count  200.000000  200.000000  200.000000  200.000000\n",
              "mean   147.042500   23.264000   30.554000   15.130500\n",
              "std     85.854236   14.846809   21.778621    5.283892\n",
              "min      0.700000    0.000000    0.300000    1.600000\n",
              "25%     74.375000    9.975000   12.750000   11.000000\n",
              "50%    149.750000   22.900000   25.750000   16.000000\n",
              "75%    218.825000   36.525000   45.100000   19.050000\n",
              "max    296.400000   49.600000  114.000000   27.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-887f2122-a8b2-4217-8211-b45b7475b855\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>TV</th>\n",
              "      <th>Radio</th>\n",
              "      <th>Newspaper</th>\n",
              "      <th>Sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>147.042500</td>\n",
              "      <td>23.264000</td>\n",
              "      <td>30.554000</td>\n",
              "      <td>15.130500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>85.854236</td>\n",
              "      <td>14.846809</td>\n",
              "      <td>21.778621</td>\n",
              "      <td>5.283892</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.700000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.300000</td>\n",
              "      <td>1.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>74.375000</td>\n",
              "      <td>9.975000</td>\n",
              "      <td>12.750000</td>\n",
              "      <td>11.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>149.750000</td>\n",
              "      <td>22.900000</td>\n",
              "      <td>25.750000</td>\n",
              "      <td>16.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>218.825000</td>\n",
              "      <td>36.525000</td>\n",
              "      <td>45.100000</td>\n",
              "      <td>19.050000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>296.400000</td>\n",
              "      <td>49.600000</td>\n",
              "      <td>114.000000</td>\n",
              "      <td>27.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-887f2122-a8b2-4217-8211-b45b7475b855')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-887f2122-a8b2-4217-8211-b45b7475b855 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-887f2122-a8b2-4217-8211-b45b7475b855');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-ce01ac35-d13c-485e-b8a6-2a878f994d52\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ce01ac35-d13c-485e-b8a6-2a878f994d52')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-ce01ac35-d13c-485e-b8a6-2a878f994d52 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "by the above table we can see that the sales are higher in tv advertisiment"
      ],
      "metadata": {
        "id": "e3e_t3FGv0O0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.pairplot(df,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',kind='scatter')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 268
        },
        "id": "UcE-qYz_wCUR",
        "outputId": "7af5e8c4-4809-423e-b4af-35290d8322a8"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 750x250 with 3 Axes>"
            ],
            "image/png": "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w4dx2223oVOnTkhMTMQtt9yC/fv3A2hbF5OTk7F582bk5ORAr9dj4sSJuHDhAvddFRUVmDZtGrp27YqEhAQMHz4cX3/9tUt7e/bsiRUrVmDWrFmIj4/HDTfcgDfffNPlGpPJhAceeABdunRBYmIixo8fj8OHD3PvL126FEOGDME777yD7Oxs6PV6b7uWuAYp5UTEMHv2bNhsNnz00UfcawzDYMOGDSgqKoJarQ5j6wgi+ikrK8PevXuh0+kAAFarFbfccgs+//xzlJWV4aGHHsJ///d/4/vvv+c+84c//AE7d+7Eli1b8J///Ac7duzAwYMHRX/D6XRi2rRpuHr1Knbu3ImvvvoKZ86cwa9//eug3x9BBBO1Wo0XX3wRb7zxBn766SeP9ysqKnDnnXdi5syZOHLkCP7xj39gz549KC4uBgCMHTsWx48fx5UrVwAAO3fuRFpaGnbs2AEAaGlpwbfffotx48YBaFsTb7zxRvzwww84cOAAFi5cCK1Wy/2exWLBH//4R7z77rsoKSmByWTCfffdx73f2NiIu+66C9u2bUNpaSnuvPNOTJ06FZWVlS7tfvXVVzF48GCUlpZi4cKFePTRR7mNOwDcc889qK6uxr/+9S8cOHAAQ4cOxe23346rV69y15SXl+Pjjz/GJ598gkOHDvnVzx0ahiBCzLp165ikpCTB9+677z5m7Nix3N/btm1jADCnT58OTeMIoh1RWFjIqNVqJj4+nomNjWUAMDExMcxHH30k+pnJkyczTzzxBMMwDNPQ0MDodDrmn//8J/d+bW0tExcXxzz66KPca1lZWcxf/vIXhmEY5j//+Q+jVquZyspK7v1jx44xAJjvv/8+sDdIECGisLCQmTZtGsMwDHPrrbcyc+fOZRiGYTZt2sSwqtS8efOYhx56yOVzu3fvZmJiYpjm5mbG6XQyqampzIcffsgwDMMMGTKEWblyJdOtWzeGYRhmz549jFarZZqamhiGYZhOnTox69evF2zPunXrGADMd999x7124sQJBgCzb98+0fvo378/88Ybb3B/Z2VlMXfeeafLNb/+9a+ZSZMmce1PTExkrFaryzW9e/dm/vd//5dhGIZZsmQJo9VqmerqatHfJZRBlnIiopg7dy527dqFiooKAMDatWsxduxYGI3GMLeMIKKT2267DYcOHcK+fftQWFiIOXPmYObM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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "the growth of sales of TV are more appropriate. when compared to radio and newspaper"
      ],
      "metadata": {
        "id": "2y4-Z-gyxOfi"
      }
    },
    {
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "df['TV'].plot.hist(bins=10)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "w4wgJPCeyMOo",
        "outputId": "befccfc1-982b-4dec-fff3-4de7312679f3"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Frequency'>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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l8ul9evXe+2fPHmyXC6X1y0tLc2XkQEAwHXIp5ApLi5WQkJCre1dunRRcXHxVT9OZWWl+vfvr8WLF1/2mLS0NJWUlHhuq1at8mVkAABwHfLpGpmoqCjl5+fX+qmkjz/+WB06dLjqx0lPT1d6enq9xwQHBysmJsaXMQEAwHXOpzMy48eP1+9+9zvt2LFD1dXVqq6u1vbt2zVz5kzde++9fh1w586dioqKUu/evfXQQw/p9OnT9R7vdrtVXl7udQMAANcnn87IPP/88zp69KhSUlLUqtUPD1FTU6P777+/QdfIXElaWprGjBmjhIQEFRUV6emnn1Z6erry8vLUsmXLOj8mOztb8+bN89sM1yMb35QMAIC6uIwxxtcP/uKLL/Txxx+rbdu26tu3r7p06eL7IC6X1q1bp1GjRl32mC+//FLdu3fX1q1blZKSUucxbrdbbrfbc7+8vFzx8fEqKytTaGioz/PVhSAAADR3jfXu1+Xl5QoLC7viv98+nZH5Ua9evdSrV69reYgG6datmyIjI1VYWHjZkAkODlZwcHCTzQQAAJzjU8hUV1crJydH27Zt06lTp1RTU+O1f/v27X4Z7qeOHz+u06dPX/a3CQMAgObFp5CZOXOmcnJyNHz4cCUmJsrlcvn0ySsqKlRYWOi5f+TIER08eFARERGKiIjQvHnzNHbsWMXExKioqEhPPPGEevTooaFDh/r0+QAAwPXFp5BZvXq13n77bQ0bNuyaPvm+fft09913e+5nZmZKkiZNmqQlS5YoPz9fy5cv19mzZxUXF6chQ4bo+eef56UjAAAgyceQCQoKUo8ePa75k991112q71rjd99995o/BwAAuH759HtkHnvsMb3yyiv1RggAAEBj8+mMzO7du7Vjxw5t2rRJN998s1q3bu21f+3atX4ZDgAAoD4+hUx4eLhGjx7t71kAAAAaxKeQWbZsmb/nAAAAaDCfrpGRpEuXLmnr1q36y1/+onPnzkmSTpw4oYqKCr8NBwAAUB+fzsh89dVXSktLU3Fxsdxut379618rJCREL774otxut5YuXervOQEAAGrx6YzMzJkzddttt+m7775T27ZtPdtHjx6tbdu2+W04AACA+vh0Rubf//63PvjgAwUFBXlt79q1q77++mu/DAYAAHAlPp2RqampUXV1da3tx48fV0hIyDUPBQAAcDV8CpkhQ4Zo0aJFnvsul0sVFRWaO3fuNb9tAQAAwNXy6aWll19+WUOHDtVNN92kCxcuaMKECTp8+LAiIyO1atUqf88IAABQJ59CplOnTvr444+1evVq5efnq6KiQlOnTtXEiRO9Lv4FAABoTD6FjCS1atVK9913nz9nAQAAaBCfQmbFihX17r///vt9GgYAAKAhfAqZmTNnet2vqqrS+fPnFRQUpHbt2hEyAACgSfj0U0vfffed162iokIFBQUaOHAgF/sCAIAm4/N7Lf1Uz549NX/+/FpnawAAABqL30JG+uEC4BMnTvjzIQEAAC7Lp2tk/vGPf3jdN8aopKREf/7zn3XnnXf6ZTAAAIAr8SlkRo0a5XXf5XKpY8eOuueee/Tyyy/7Yy4AAIAr8ilkampq/D0HAABAg/n1GhkAAICm5NMZmczMzKs+duHChb58CgAAgCvyKWQOHDigAwcOqKqqSr1795YkffHFF2rZsqVuvfVWz3Eul8s/UwIAANTBp5AZMWKEQkJCtHz5ct14442SfvgleVOmTNGgQYP02GOP+XVIAACAuvh0jczLL7+s7OxsT8RI0o033qgXXniBn1oCAABNxqeQKS8v1zfffFNr+zfffKNz585d81AAAABXw6eQGT16tKZMmaK1a9fq+PHjOn78uP7+979r6tSpGjNmjL9nBAAAqJNP18gsXbpUs2fP1oQJE1RVVfXDA7VqpalTp+qll17y64AAAACX41PItGvXTq+99ppeeuklFRUVSZK6d++uG264wa/DAQAA1OeafiFeSUmJSkpK1LNnT91www0yxvhrLgAAgCvyKWROnz6tlJQU9erVS8OGDVNJSYkkaerUqfzoNQAAaDI+hcyjjz6q1q1bq7i4WO3atfNsHzdunDZv3uy34QAAAOrj0zUy7733nt5991116tTJa3vPnj311Vdf+WUwAACAK/HpjExlZaXXmZgfnTlzRsHBwdc8FAAAwNXwKWQGDRqkFStWeO67XC7V1NRowYIFuvvuu/02HAAAQH18emlpwYIFSklJ0b59+3Tx4kU98cQT+vTTT3XmzBm9//77/p4RAACgTj6dkUlMTNQXX3yhgQMHauTIkaqsrNSYMWN04MABde/e3d8zAgAA1KnBZ2SqqqqUlpampUuX6ve//31jzAQAAHBVGnxGpnXr1srPz2+MWQAAABrEp5eW7rvv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VVVpyJAhqqys9Bxzpe/B6upqDR8+XBcvXtQHH3yg5cuXKycnR3PmzHHiS2pUV7NekvTggw96PccWLFjg2dec1kuSOnXqpPnz52v//v3at2+f7rnnHo0cOVKffvqpJAefXwYNcscdd5iMjAzP/erqahMXF2eys7MdnCowzJ071/Tv37/OfWfPnjWtW7c2a9as8Wz773//aySZvLy8JpowcEgy69at89yvqakxMTEx5qWXXvJsO3v2rAkODjarVq0yxhjz2WefGUnmP//5j+eYTZs2GZfLZb7++usmm90JP10vY4yZNGmSGTly5GU/pjmvlzHGnDp1ykgyubm5xpir+x7817/+ZVq0aGFKS0s9xyxZssSEhoYat9vdtF9AE/vpehljzK9+9Sszc+bMy35Mc16vH914443mr3/9q6PPL87INMDFixe1f/9+paamera1aNFCqampysvLc3CywHH48GHFxcWpW7dumjhxooqLiyVJ+/fvV1VVldfa9enTR507d2btJB05ckSlpaVe6xMWFqakpCTP+uTl5Sk8PFy33Xab55jU1FS1aNFCe/fubfKZA8HOnTsVFRWl3r1766GHHtLp06c9+5r7epWVlUmSIiIiJF3d92BeXp769u3r9QtHhw4dqvLycs//uq9XP12vH7355puKjIxUYmKisrKydP78ec++5rxe1dXVWr16tSorK5WcnOzo8yvgf7NvIPn2229VXV1d67cKR0dH6/PPP3doqsCRlJSknJwc9e7dWyUlJZo3b54GDRqkQ4cOqbS0VEFBQbXewDM6OlqlpaXODBxAflyDup5bP+4rLS1VVFSU1/5WrVopIiKiWa5hWlqaxowZo4SEBBUVFenpp59Wenq68vLy1LJly2a9XjU1NZo1a5buvPNOJSYmStJVfQ+WlpbW+Rz8cd/1qq71kqQJEyaoS5cuiouLU35+vp588kkVFBRo7dq1kprnen3yySdKTk7WhQsX1L59e61bt0433XSTDh486Njzi5CB36Snp3v+3K9fPyUlJalLly56++231bZtWwcnw/Xo3nvv9fy5b9++6tevn7p3766dO3cqJSXFwcmcl5GRoUOHDnldo4bLu9x6/e/1VH379lVsbKxSUlJUVFSk7t27N/WYAaF37946ePCgysrK9Le//U2TJk1Sbm6uozPx0lIDREZGqmXLlrWuwj558qRiYmIcmipwhYeHq1evXiosLFRMTIwuXryos2fPeh3D2v3gxzWo77kVExNT66LyS5cu6cyZM6yhpG7duikyMlKFhYWSmu96zZgxQxs3btSOHTvUqVMnz/ar+R6MiYmp8zn4477r0eXWqy5JSUmS5PUca27rFRQUpB49emjAgAHKzs5W//799corrzj6/CJkGiAoKEgDBgzQtm3bPNtqamq0bds2JScnOzhZYKqoqFBRUZFiY2M1YMAAtW7d2mvtCgoKVFxczNpJSkhIUExMjNf6lJeXa+/evZ71SU5O1tmzZ7V//37PMdu3b1dNTY3nL9jm7Pjx4zp9+rRiY2MlNb/1MsZoxowZWrdunbZv366EhASv/VfzPZicnKxPPvnEKwC3bNmi0NBQ3XTTTU3zhTSRK61XXQ4ePChJXs+x5rJel1NTUyO32+3s88vny4SbqdWrV5vg4GCTk5NjPvvsMzNt2jQTHh7udRV2c/XYY4+ZnTt3miNHjpj333/fpKammsjISHPq1CljjDHTp083nTt3Ntu3bzf79u0zycnJJjk52eGpm865c+fMgQMHzIEDB4wks3DhQnPgwAHz1VdfGWOMmT9/vgkPDzcbNmww+fn5ZuTIkSYhIcF8//33nsdIS0szv/jFL8zevXvN7t27Tc+ePc348eOd+pIaVX3rde7cOTN79myTl5dnjhw5YrZu3WpuvfVW07NnT3PhwgXPYzSn9XrooYdMWFiY2blzpykpKfHczp8/7znmSt+Dly5dMomJiWbIkCHm4MGDZvPmzaZjx44mKyvLiS+pUV1pvQoLC80f/vAHs2/fPnPkyBGzYcMG061bNzN48GDPYzSn9TLGmKeeesrk5uaaI0eOmPz8fPPUU08Zl8tl3nvvPWOMc88vQsYHf/rTn0znzp1NUFCQueOOO8yePXucHikgjBs3zsTGxpqgoCDzs5/9zIwbN84UFhZ69n///ffm4YcfNjfeeKNp166dGT16tCkpKXFw4qa1Y8cOI6nWbdKkScaYH34E+9lnnzXR0dEmODjYpKSkmIKCAq/HOH36tBk/frxp3769CQ0NNVOmTDHnzp1z4KtpfPWt1/nz582QIUNMx44dTevWrU2XLl3Mgw8+WOs/FM1pvepaK0lm2bJlnmOu5nvw6NGjJj093bRt29ZERkaaxx57zFRVVTXxV9P4rrRexcXFZvDgwSYiIsIEBwebHj16mMcff9yUlZV5PU5zWS9jjHnggQdMly5dTFBQkOnYsaNJSUnxRIwxzj2/XMYY4/v5HAAAAOdwjQwAALAWIQMAAKxFyAAAAGsRMgAAwFqEDAAAsBYhAwAArEXIAAAAaxEyAADAWoQMAACwFiEDAACsRcgAAABrETIAAMBa/w/Ucm8T/i/aFQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Radio'].plot.hist(bins=10, color=\"Red\", xlabel=\"Radio\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "vTX65Ia0yQCa",
        "outputId": "69e7e60d-26a8-4ac9-e820-71bda3e428c6"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Frequency'>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ebVt21YulytsP8fn8yktLU2nT59WfHx82PaL6hjrhsNYNxzGuuEw1g0nnGNtjNHFixeVmpp63e2iusi0a9dOTZs2VVlZWdDysrIyJScn1/gat9stt9sdtKx169aRiqj4+Hh+MRoIY91wGOuGw1g3HMa64YRrrK93JuYHUX2xb2xsrPr166fc3NzAsqqqKuXm5iojI8PBZAAAIBpE9RkZScrOztaUKVN0xx136K677tLLL7+s8vJyTZs2zeloAADAYVFfZCZMmKBz587pueeeU2lpqW6//XZt3ry52gXADc3tdmvBggXVPsZC+DHWDYexbjiMdcNhrBuOE2PtMj91XxMAAECUiuprZAAAAK6HIgMAAKxFkQEAANaiyAAAAGtRZEK0fPlyde7cWc2bN1f//v318ccfOx3Jert27dKoUaOUmpoql8uljRs3Bq03xui5555TSkqKWrRooczMTB0/ftyZsJbLycnRnXfeqbi4OCUmJmrMmDEqLCwM2ubKlSvKyspS27Zt1apVK40fP77awylxfa+++qp69+4deDhYRkaGNm3aFFjPGEfOokWL5HK5NHv27MAyxjs8nn/+eblcrqCpZ8+egfUNPc4UmRC8/fbbys7O1oIFC7R//3716dNHw4YN09mzZ52OZrXy8nL16dNHy5cvr3H94sWLtWzZMq1YsUJ79+7VTTfdpGHDhunKlSsNnNR+eXl5ysrK0p49e7R161ZVVFRo6NChKi8vD2wzZ84cvffee1q3bp3y8vJUXFyscePGOZjaPh06dNCiRYtUUFCgffv2afDgwRo9erQ+++wzSYxxpHzyySd67bXX1Lt376DljHf43HbbbSopKQlMu3fvDqxr8HE2qLe77rrLZGVlBeYrKytNamqqycnJcTBV4yLJbNiwITBfVVVlkpOTzUsvvRRYduHCBeN2u81bb73lQMLG5ezZs0aSycvLM8ZcG9tmzZqZdevWBbb597//bSSZ/Px8p2I2Cm3atDF/+ctfGOMIuXjxounWrZvZunWr+b//+z8za9YsYwzHdDgtWLDA9OnTp8Z1TowzZ2Tq6erVqyooKFBmZmZgWZMmTZSZman8/HwHkzVup06dUmlpadC4ezwe9e/fn3EPA6/XK0lKSEiQJBUUFKiioiJovHv27KmOHTsy3iGqrKzU2rVrVV5eroyMDMY4QrKysnT//fcHjavEMR1ux48fV2pqqm6++WZNnDhRRUVFkpwZ56h/sm+0+frrr1VZWVntycJJSUk6evSoQ6kav9LSUkmqcdx/WIfQVFVVafbs2RowYIB69eol6dp4x8bGVvvCVca7/g4fPqyMjAxduXJFrVq10oYNG3Trrbfq4MGDjHGYrV27Vvv379cnn3xSbR3HdPj0799fq1atUo8ePVRSUqKFCxdq0KBBOnLkiCPjTJEB/sdlZWXpyJEjQZ9xI3x69OihgwcPyuv16u9//7umTJmivLw8p2M1OqdPn9asWbO0detWNW/e3Ok4jdqIESMC/927d2/1799fnTp10jvvvKMWLVo0eB4+Wqqndu3aqWnTptWuwC4rK1NycrJDqRq/H8aWcQ+vmTNn6v3339eOHTvUoUOHwPLk5GRdvXpVFy5cCNqe8a6/2NhYde3aVf369VNOTo769OmjpUuXMsZhVlBQoLNnz6pv376KiYlRTEyM8vLytGzZMsXExCgpKYnxjpDWrVure/fuOnHihCPHNUWmnmJjY9WvXz/l5uYGllVVVSk3N1cZGRkOJmvc0tPTlZycHDTuPp9Pe/fuZdxDYIzRzJkztWHDBm3fvl3p6elB6/v166dmzZoFjXdhYaGKiooY7xtUVVUlv9/PGIfZkCFDdPjwYR08eDAw3XHHHZo4cWLgvxnvyLh06ZJOnjyplJQUZ47riFxC3MitXbvWuN1us2rVKvP555+bxx57zLRu3dqUlpY6Hc1qFy9eNAcOHDAHDhwwksySJUvMgQMHzFdffWWMMWbRokWmdevW5t133zWHDh0yo0ePNunp6ea7775zOLl9Hn/8cePxeMzOnTtNSUlJYLp8+XJgmxkzZpiOHTua7du3m3379pmMjAyTkZHhYGr7PP300yYvL8+cOnXKHDp0yDz99NPG5XKZDz74wBjDGEfaf9+1ZAzjHS5z5841O3fuNKdOnTIffvihyczMNO3atTNnz541xjT8OFNkQvSnP/3JdOzY0cTGxpq77rrL7Nmzx+lI1tuxY4eRVG2aMmWKMebaLdjPPvusSUpKMm632wwZMsQUFhY6G9pSNY2zJLNy5crANt9995154oknTJs2bUzLli3N2LFjTUlJiXOhLfTII4+YTp06mdjYWNO+fXszZMiQQIkxhjGOtB8XGcY7PCZMmGBSUlJMbGys+dnPfmYmTJhgTpw4EVjf0OPsMsaYyJzrAQAAiCyukQEAANaiyAAAAGtRZAAAgLUoMgAAwFoUGQAAYC2KDAAAsBZFBgAAWIsiAwAArEWRAQAA1qLIAAAAa1FkAACAtSgyAADAWv8Pyu3/u+Be02YAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Newspaper'].plot.hist(bins=10, color=\"black\", xlabel=\"Newspaper\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "kMcGSxkJytEv",
        "outputId": "313d7a6b-e436-455d-8a3d-5e521d9c09ca"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Frequency'>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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vHmzNm/erKamJl1wwQWSpB07dqhdu3YaMGCA/3XcMA4AAJxKQYXM9ddfr9jYWL3yyiv+u/x+//33mjJliq666irdfffdIR0SAADgWIL6iIJzzjlH77//vi6++OKA7du2bdN1110XVveS4SMKgJbjIwoAhItT+hEFXq9X+/fvP2r7/v37VVdXF8wuAQAAWi2okBk3bpymTJmipUuXau/evdq7d6/+/ve/a+rUqRo/fnyoZwQAADimoM6RmTdvnu655x79+te/VlNT05EdRUZq6tSpevrpp0M6IAAAwPEEdY7MTw4ePKivvvpKknTeeeepU6dOIRssVDhHBmg5zpEBEC5O6TkyP6msrFRlZaV69+6tTp068UMQAACcVkGFzHfffadhw4bp/PPP16hRo1RZWSlJmjp1KpdeAwCA0yaokJk5c6aioqJUXl6ujh07+rffeOONeu+990I2HAAAwIkEdbLv+++/rxUrVqh79+4B23v37q2vv/46JIMBAAD8nKCOyBw8eDDgSMxPDhw4oJiYmJMeCgAAoCWCCpmrrrpKCxcu9H/tcrnk8/n01FNP6eqrrw7ZcAAAACcS1FtLTz31lIYNG6aNGzfq0KFDuvfee/X555/rwIED+te//hXqGQEAAI4pqCMyffv21Y4dOzR06FCNGTNGBw8e1Pjx47V582add955oZ4RAADgmFp9RKapqUkjRozQvHnz9OCDD56KmQAAAFqk1SETFRWlrVu3nopZADjMxrtVcyNO4MwW1FtLkyZN0ssvvxzqWQAAAFolqJN9Dx8+rPnz5+vDDz9Uenr6UZ+xVFBQEJLhAAAATqRVR2R27doln8+nbdu2acCAAYqNjdWOHTu0efNm/6O0tLTF+8vPz9fll1+u2NhYJSYmauzYsSorKwt4TUNDg3JycpSQkKDOnTsrKytL1dXVrRkbAAC0Ua369Ot27dqpsrJSiYmJko58JMHcuXOVlJQU1B8+YsQITZgwQZdffrkOHz6sBx54QNu2bdMXX3zhP8pzxx136B//+IcWLFggj8ejadOmKSIiosWXefPp10DbxjkyQNvU0t/frQqZiIgIVVVV+UPG7XartLRU55577slPLGn//v1KTEzU6tWr9X//93+qra3V2WefrUWLFumGG26QJG3fvl0XXnihiouLNXjw4J/dJyEDtG2EDNA2tfT3d1An+/4k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O6/Xq3Xr1p3xaydJP/zwgyIiAn8ttGvXTj6fTxLr11ItWaeMjAzV1NSopKTE/5qVK1fK5/Np0KBBp31mqzl9trFtFi9ebGJiYsyCBQvMF198YW677TYTFxdnqqqqnB4trNxxxx3G4/GYjz76yFRWVvofP/zwg/81t99+u0lNTTUrV640GzduNBkZGSYjI8PBqcPXf1+1ZAxrdzzr1683kZGR5vHHHzc7d+40r732munYsaN59dVX/a+ZPXu2iYuLM2+++abZunWrGTNmzBl5+fCxZGdnm3POOcd/+fXSpUtNly5dzL333ut/Det3RF1dndm8ebPZvHmzkWQKCgrM5s2bzddff22Madk6jRgxwlx22WVm3bp1Zu3ataZ3795cfh0EQiYIf/rTn0xqaqqJjo42V1xxhfn000+dHinsSDrmo7Cw0P+aH3/80dx5553mrLPOMh07djTjxo0zlZWVzg0dxv43ZFi743v77bdN3759TUxMjOnTp4/5y1/+EvC8z+czDz30kElKSjIxMTFm2LBhpqyszKFpw4vX6zW5ubkmNTXVtG/f3px77rnmwQcfNI2Njf7XsH5HrFq16pg/47Kzs40xLVun7777ztx0002mc+fOxu12mylTppi6ujoH/jZ2cxnzX7dsBAAAsAjnyAAAAGsRMgAAwFqEDAAAsBYhAwAArEXIAAAAaxEyAADAWoQMAACwFiEDAACsRcgAAABrETIAAMBahAwAALAWIQMAAKz1/wCc+8oVMQ7vMgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(df.corr(),annot=True)\n",
        "plt.show"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "id": "bpFKXh9_zIy-",
        "outputId": "f8ae314d-3586-4f69-d54a-8e5bbd9fd2f7"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<function matplotlib.pyplot.show(close=None, block=None)>"
            ]
          },
          "metadata": {},
          "execution_count": 25
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "by observing the heatmap. we can conclude the TV are having high sales"
      ],
      "metadata": {
        "id": "L_jWs6_2zmNb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train, x_test, y_train, y_test = train_test_split(df[['TV']], df[['Sales']], test_size=0.3, random_state=0)"
      ],
      "metadata": {
        "id": "rqOqwCpVz3-9"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EjHzQFN61JOW",
        "outputId": "c0348e73-e0fe-4ad2-81b2-9f237c857a16"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        TV\n",
            "131  265.2\n",
            "96   197.6\n",
            "181  218.5\n",
            "19   147.3\n",
            "153  171.3\n",
            "..     ...\n",
            "67   139.3\n",
            "192   17.2\n",
            "117   76.4\n",
            "47   239.9\n",
            "172   19.6\n",
            "\n",
            "[140 rows x 1 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "40yfdsw21QNu",
        "outputId": "a7360025-7c6f-4e19-adcf-1a57e808fc03"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Sales\n",
            "131   17.7\n",
            "96    16.7\n",
            "181   17.2\n",
            "19    14.6\n",
            "153   16.0\n",
            "..     ...\n",
            "67    13.4\n",
            "192    5.9\n",
            "117    9.4\n",
            "47    23.2\n",
            "172    7.6\n",
            "\n",
            "[140 rows x 1 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(x_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "glAFffVi1QDl",
        "outputId": "e5228262-1efd-4848-9fec-dc42ed01c069"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        TV\n",
            "18    69.2\n",
            "170   50.0\n",
            "107   90.4\n",
            "98   289.7\n",
            "177  170.2\n",
            "182   56.2\n",
            "5      8.7\n",
            "146  240.1\n",
            "12    23.8\n",
            "152  197.6\n",
            "61   261.3\n",
            "125   87.2\n",
            "180  156.6\n",
            "154  187.8\n",
            "80    76.4\n",
            "7    120.2\n",
            "33   265.6\n",
            "130    0.7\n",
            "37    74.7\n",
            "74   213.4\n",
            "183  287.6\n",
            "145  140.3\n",
            "45   175.1\n",
            "159  131.7\n",
            "60    53.5\n",
            "123  123.1\n",
            "179  165.6\n",
            "185  205.0\n",
            "122  224.0\n",
            "44    25.1\n",
            "16    67.8\n",
            "55   198.9\n",
            "150  280.7\n",
            "111  241.7\n",
            "22    13.2\n",
            "189   18.7\n",
            "129   59.6\n",
            "4    180.8\n",
            "83    68.4\n",
            "106   25.0\n",
            "134   36.9\n",
            "66    31.5\n",
            "26   142.9\n",
            "113  209.6\n",
            "168  215.4\n",
            "63   102.7\n",
            "8      8.6\n",
            "75    16.9\n",
            "118  125.7\n",
            "143  104.6\n",
            "71   109.8\n",
            "124  229.5\n",
            "184  253.8\n",
            "97   184.9\n",
            "149   44.7\n",
            "24    62.3\n",
            "30   292.9\n",
            "160  172.5\n",
            "40   202.5\n",
            "56     7.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zvJQ9gj-1Z8P",
        "outputId": "50e5b032-724a-4805-faa6-d64f57a6c79b"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Sales\n",
            "18    11.3\n",
            "170    8.4\n",
            "107   12.0\n",
            "98    25.4\n",
            "177   16.7\n",
            "182    8.7\n",
            "5      7.2\n",
            "146   18.2\n",
            "12     9.2\n",
            "152   16.6\n",
            "61    24.2\n",
            "125   10.6\n",
            "180   15.5\n",
            "154   20.6\n",
            "80    11.8\n",
            "7     13.2\n",
            "33    17.4\n",
            "130    1.6\n",
            "37    14.7\n",
            "74    17.0\n",
            "183   26.2\n",
            "145   10.3\n",
            "45    16.1\n",
            "159   12.9\n",
            "60     8.1\n",
            "123   15.2\n",
            "179   17.6\n",
            "185   22.6\n",
            "122   16.6\n",
            "44     8.5\n",
            "16    12.5\n",
            "55    23.7\n",
            "150   16.1\n",
            "111   21.8\n",
            "22     5.6\n",
            "189    6.7\n",
            "129    9.7\n",
            "4     17.9\n",
            "83    13.6\n",
            "106    7.2\n",
            "134   10.8\n",
            "66    11.0\n",
            "26    15.0\n",
            "113   20.9\n",
            "168   17.1\n",
            "63    14.0\n",
            "8      4.8\n",
            "75     8.7\n",
            "118   15.9\n",
            "143   10.4\n",
            "71    12.4\n",
            "124   19.7\n",
            "184   17.6\n",
            "97    20.5\n",
            "149   10.1\n",
            "24     9.7\n",
            "30    21.4\n",
            "160   16.4\n",
            "40    16.6\n",
            "56     5.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "model=LinearRegression()\n",
        "model.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "6Dz2N6VX1hNd",
        "outputId": "dfd9bcb0-a48f-4d35-a000-cc5c3d3a480b"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res=model.predict(x_test)\n",
        "print(res)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B-D5f_In18Gx",
        "outputId": "c08ab09c-a68f-4b95-c971-8fc9cf6d9028"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[10.93127621]\n",
            " [ 9.88042193]\n",
            " [12.09159447]\n",
            " [22.99968079]\n",
            " [16.45920756]\n",
            " [10.21976029]\n",
            " [ 7.6199906 ]\n",
            " [20.28497391]\n",
            " [ 8.4464437 ]\n",
            " [17.95886418]\n",
            " [21.44529217]\n",
            " [11.91645209]\n",
            " [15.71485245]\n",
            " [17.42249065]\n",
            " [11.32534656]\n",
            " [13.72260788]\n",
            " [21.68063975]\n",
            " [ 7.18213465]\n",
            " [11.23230217]\n",
            " [18.82362968]\n",
            " [22.88474361]\n",
            " [14.82272095]\n",
            " [16.72739433]\n",
            " [14.35202581]\n",
            " [10.07198391]\n",
            " [13.88133066]\n",
            " [16.20744039]\n",
            " [18.36388094]\n",
            " [19.40378881]\n",
            " [ 8.51759529]\n",
            " [10.85465142]\n",
            " [18.03001578]\n",
            " [22.50709285]\n",
            " [20.3725451 ]\n",
            " [ 7.86628457]\n",
            " [ 8.16731053]\n",
            " [10.40584907]\n",
            " [17.03936669]\n",
            " [10.88749061]\n",
            " [ 8.51212209]\n",
            " [ 9.16343282]\n",
            " [ 8.86788005]\n",
            " [14.96502414]\n",
            " [18.61564811]\n",
            " [18.93309367]\n",
            " [12.76479799]\n",
            " [ 7.6145174 ]\n",
            " [ 8.06879294]\n",
            " [14.02363385]\n",
            " [12.86878878]\n",
            " [13.15339515]\n",
            " [19.70481478]\n",
            " [21.03480222]\n",
            " [17.26376787]\n",
            " [ 9.59034237]\n",
            " [10.55362545]\n",
            " [23.17482317]\n",
            " [16.58509115]\n",
            " [18.22705095]\n",
            " [ 7.54336581]]\n"
          ]
        }
      ]
    },
    {
      "source": [
        "print(model.coef_)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g8bxzx3g2bFO",
        "outputId": "d1045bc6-69ef-4db2-bc19-b20844f63e3b"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0.05473199]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(model.intercept_)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vnj0Ajrz2efc",
        "outputId": "44a306fe-eadc-49ed-9701-8617831b889d"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[7.14382225]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "0.05473199*50+7.14382225"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OdhNm27y2l0m",
        "outputId": "743d3948-b7d8-46a5-ae74-38851f4f1b5b"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9.88042175"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.plot(res)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "KUfxKQLg3Az-",
        "outputId": "b79bc8a1-d171-4902-b6eb-3cbce453540e"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x78d9cbf39000>]"
            ]
          },
          "metadata": {},
          "execution_count": 42
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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hBZdcskl+P73vy8+zq9Xaz73uc9B0zTccMMN4u/4NTP59Kc/DU3Tav6cccYZ4uP8WjXmlVdewfve9z6MjIygu7sb5557LrZv3y4+rvLav2CKj29+85u48cYb8alPfQo7duzAhg0bcNVVV2F8fDzoQwucbDaLDRs24Lbbbmv48c9//vP48pe/jDvuuAOPP/44ent7cdVVV2Fubs7nIw0H27Ztw5YtW/DYY4/hoYceQrFYxJVXXolsNis+5+Mf/zgeeOABfOtb38K2bdtw6NAhvPOd7wzwqINl5cqV+NznPocnnngC27dvxxvf+EZce+21ePbZZwHw69WKX//61/iHf/gHnHfeeTV/z69ZLWeffTYOHz4s/vz85z8XH+PXaj7Hjx/HpZdeimQyie9///t47rnn8Nd//ddYtGiR+Byl135jgfDqV7/a2LJli/jvcrlsrFixwti6dWuARxU+ABj33nuv+G9d141ly5YZ//f//l/xdydOnDDS6bTxr//6rwEcYfgYHx83ABjbtm0zDKPy+iSTSeNb3/qW+Jznn3/eAGA8+uijQR1m6Fi0aJHxz//8z/x6tWBmZsY49dRTjYceesh4/etfb/zxH/+xYRh8jtXzqU99ytiwYUPDj/Fr1ZhPfvKTxmWXXdb046qv/QtC+SgUCnjiiSdwxRVXiL+LxWK44oor8OijjwZ4ZOFn3759GBsbq3ntBgcHcfHFF/NrV2VqagoAMDw8DAB44oknUCwWa16zM844A6tXr+bXDEC5XMY999yDbDaLSy65hF+vFmzZsgVXX311zWsD8DnWiN27d2PFihVYt24d3vve9+LAgQMA+LVqxv33348LL7wQv/M7v4MlS5Zg48aN+Kd/+ifxcdXX/gVRfExMTKBcLmPp0qU1f7906VKMjY0FdFTRgF4ffu0ao+s6brjhBlx66aU455xzAFRes1QqhaGhoZrPXeiv2dNPP42+vj6k02l8+MMfxr333ouzzjqLX68m3HPPPdixYwe2bt0672P8mtVy8cUX46677sKDDz6I22+/Hfv27cPrXvc6zMzM8GvVhBdffBG33347Tj31VPzgBz/ARz7yEXzsYx/D1772NQDqr/2h22rLMFFiy5YteOaZZ2r6y0xjTj/9dOzcuRNTU1P493//d1x33XXYtm1b0IcVSg4ePIg//uM/xkMPPYSurq6gDyf0bN68Wfz/8847DxdffDHWrFmDf/u3f0N3d3eARxZedF3HhRdeiL/8y78EAGzcuBHPPPMM7rjjDlx33XXKv/+CUD5GR0cRj8fnuZuPHDmCZcuWBXRU0YBeH37t5nP99dfju9/9Ln7yk59g5cqV4u+XLVuGQqGAEydO1Hz+Qn/NUqkUTjnlFFxwwQXYunUrNmzYgL/927/l16sBTzzxBMbHx/GqV70KiUQCiUQC27Ztw5e//GUkEgksXbqUX7MWDA0N4bTTTsOePXv4/GrC8uXLcdZZZ9X83ZlnninaVaqv/Qui+EilUrjgggvw8MMPi7/TdR0PP/wwLrnkkgCPLPysXbsWy5Ytq3ntpqen8fjjjy/Y184wDFx//fW499578eMf/xhr166t+fgFF1yAZDJZ85rt2rULBw4cWLCvWSN0XUc+n+fXqwFvetOb8PTTT2Pnzp3iz4UXXoj3vve94v/za9acTCaDvXv3Yvny5Xx+NeHSSy+dFxHwwgsvYM2aNQB8uPZ7tqxGhHvuucdIp9PGXXfdZTz33HPGhz70IWNoaMgYGxsL+tACZ2ZmxnjyySeNJ5980gBgfPGLXzSefPJJY//+/YZhGMbnPvc5Y2hoyPjOd75jPPXUU8a1115rrF271pidnQ34yIPhIx/5iDE4OGj89Kc/NQ4fPiz+5HI58Tkf/vCHjdWrVxs//vGPje3btxuXXHKJcckllwR41MFy0003Gdu2bTP27dtnPPXUU8ZNN91kaJpm/PCHPzQMg18vO1inXQyDXzMrf/Inf2L89Kc/Nfbt22f84he/MK644gpjdHTUGB8fNwyDX6tG/OpXvzISiYTx2c9+1ti9e7fxL//yL0ZPT4/xjW98Q3yOymv/gik+DMMwvvKVrxirV682UqmU8epXv9p47LHHgj6kUPCTn/zEADDvz3XXXWcYRmXk6pZbbjGWLl1qpNNp401vepOxa9euYA86QBq9VgCMO++8U3zO7Oys8Ud/9EfGokWLjJ6eHuMd73iHcfjw4eAOOmA++MEPGmvWrDFSqZSxePFi401vepMoPAyDXy871Bcf/JqZvOc97zGWL19upFIp46STTjLe8573GHv27BEf59eqMQ888IBxzjnnGOl02jjjjDOMf/zHf6z5uMprv2YYhuFdP2EYhmEYhrHHgvB8MAzDMAwTHrj4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV7j4YBiGYRjGV/5/54Y46TK4W/4AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(x_test,y_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "VS--WY5X3Gwr",
        "outputId": "0309def5-885f-432c-a146-8eec6380d9f2"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.collections.PathCollection at 0x78d9cbf02860>"
            ]
          },
          "metadata": {},
          "execution_count": 44
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(x_test,y_test)\n",
        "plt.plot(x_test,7.14382225+0.05473199*x_test,'r')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "9bOJzvRf3QGw",
        "outputId": "6c95bc3b-3f1d-4a09-e9dd-7a191093ea5a"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "CONCLUSION : the above mention solution is successfully able to predict the sales using advertising platform dataset\n"
      ],
      "metadata": {
        "id": "Tl27Tr4i38e_"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Z-OJoJYB4a8G"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}