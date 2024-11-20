{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNMaOhU/1Av3SATc9stsl8K",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivanswamynathan/Entrans/blob/main/DS_PROJECT.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "aRt4hRacRJAR"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Reading data"
      ],
      "metadata": {
        "id": "SeZK98WCqUtK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Dataset = pd.read_csv('sales_data - sales_data.csv')\n",
        "df = pd.DataFrame(Dataset)\n",
        "df.head()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "qtEN9SCKRzsj",
        "outputId": "0537d722-4d43-4c25-f363-c77f0beb9441"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         Date  Day     Month  Year  Customer_Age       Age_Group  \\\n",
              "0  2013-11-26   26  November  2013            19     Youth (<25)   \n",
              "1  2015-11-26   26  November  2015            19     Youth (<25)   \n",
              "2  2014-03-23   23     March  2014            49  Adults (35-64)   \n",
              "3  2016-03-23   23     March  2016            49  Adults (35-64)   \n",
              "4  2014-05-15   15       May  2014            47  Adults (35-64)   \n",
              "\n",
              "  Customer_Gender    Country             State Product_Category Sub_Category  \\\n",
              "0               M     Canada  British Columbia      Accessories   Bike Racks   \n",
              "1               M     Canada  British Columbia      Accessories   Bike Racks   \n",
              "2               M  Australia   New South Wales      Accessories   Bike Racks   \n",
              "3               M  Australia   New South Wales      Accessories   Bike Racks   \n",
              "4               F  Australia   New South Wales      Accessories   Bike Racks   \n",
              "\n",
              "               Product  Order_Quantity  Unit_Cost  Unit_Price  Profit  Cost  \\\n",
              "0  Hitch Rack - 4-Bike               8         45         120     590   360   \n",
              "1  Hitch Rack - 4-Bike               8         45         120     590   360   \n",
              "2  Hitch Rack - 4-Bike              23         45         120    1366  1035   \n",
              "3  Hitch Rack - 4-Bike              20         45         120    1188   900   \n",
              "4  Hitch Rack - 4-Bike               4         45         120     238   180   \n",
              "\n",
              "   Revenue  \n",
              "0      950  \n",
              "1      950  \n",
              "2     2401  \n",
              "3     2088  \n",
              "4      418  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-aea49ad5-f71f-4091-9239-d9a520f83361\" class=\"colab-df-container\">\n",
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
              "      <th>Date</th>\n",
              "      <th>Day</th>\n",
              "      <th>Month</th>\n",
              "      <th>Year</th>\n",
              "      <th>Customer_Age</th>\n",
              "      <th>Age_Group</th>\n",
              "      <th>Customer_Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Product_Category</th>\n",
              "      <th>Sub_Category</th>\n",
              "      <th>Product</th>\n",
              "      <th>Order_Quantity</th>\n",
              "      <th>Unit_Cost</th>\n",
              "      <th>Unit_Price</th>\n",
              "      <th>Profit</th>\n",
              "      <th>Cost</th>\n",
              "      <th>Revenue</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2013-11-26</td>\n",
              "      <td>26</td>\n",
              "      <td>November</td>\n",
              "      <td>2013</td>\n",
              "      <td>19</td>\n",
              "      <td>Youth (&lt;25)</td>\n",
              "      <td>M</td>\n",
              "      <td>Canada</td>\n",
              "      <td>British Columbia</td>\n",
              "      <td>Accessories</td>\n",
              "      <td>Bike Racks</td>\n",
              "      <td>Hitch Rack - 4-Bike</td>\n",
              "      <td>8</td>\n",
              "      <td>45</td>\n",
              "      <td>120</td>\n",
              "      <td>590</td>\n",
              "      <td>360</td>\n",
              "      <td>950</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2015-11-26</td>\n",
              "      <td>26</td>\n",
              "      <td>November</td>\n",
              "      <td>2015</td>\n",
              "      <td>19</td>\n",
              "      <td>Youth (&lt;25)</td>\n",
              "      <td>M</td>\n",
              "      <td>Canada</td>\n",
              "      <td>British Columbia</td>\n",
              "      <td>Accessories</td>\n",
              "      <td>Bike Racks</td>\n",
              "      <td>Hitch Rack - 4-Bike</td>\n",
              "      <td>8</td>\n",
              "      <td>45</td>\n",
              "      <td>120</td>\n",
              "      <td>590</td>\n",
              "      <td>360</td>\n",
              "      <td>950</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2014-03-23</td>\n",
              "      <td>23</td>\n",
              "      <td>March</td>\n",
              "      <td>2014</td>\n",
              "      <td>49</td>\n",
              "      <td>Adults (35-64)</td>\n",
              "      <td>M</td>\n",
              "      <td>Australia</td>\n",
              "      <td>New South Wales</td>\n",
              "      <td>Accessories</td>\n",
              "      <td>Bike Racks</td>\n",
              "      <td>Hitch Rack - 4-Bike</td>\n",
              "      <td>23</td>\n",
              "      <td>45</td>\n",
              "      <td>120</td>\n",
              "      <td>1366</td>\n",
              "      <td>1035</td>\n",
              "      <td>2401</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2016-03-23</td>\n",
              "      <td>23</td>\n",
              "      <td>March</td>\n",
              "      <td>2016</td>\n",
              "      <td>49</td>\n",
              "      <td>Adults (35-64)</td>\n",
              "      <td>M</td>\n",
              "      <td>Australia</td>\n",
              "      <td>New South Wales</td>\n",
              "      <td>Accessories</td>\n",
              "      <td>Bike Racks</td>\n",
              "      <td>Hitch Rack - 4-Bike</td>\n",
              "      <td>20</td>\n",
              "      <td>45</td>\n",
              "      <td>120</td>\n",
              "      <td>1188</td>\n",
              "      <td>900</td>\n",
              "      <td>2088</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2014-05-15</td>\n",
              "      <td>15</td>\n",
              "      <td>May</td>\n",
              "      <td>2014</td>\n",
              "      <td>47</td>\n",
              "      <td>Adults (35-64)</td>\n",
              "      <td>F</td>\n",
              "      <td>Australia</td>\n",
              "      <td>New South Wales</td>\n",
              "      <td>Accessories</td>\n",
              "      <td>Bike Racks</td>\n",
              "      <td>Hitch Rack - 4-Bike</td>\n",
              "      <td>4</td>\n",
              "      <td>45</td>\n",
              "      <td>120</td>\n",
              "      <td>238</td>\n",
              "      <td>180</td>\n",
              "      <td>418</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-aea49ad5-f71f-4091-9239-d9a520f83361')\"\n",
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
              "        document.querySelector('#df-aea49ad5-f71f-4091-9239-d9a520f83361 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-aea49ad5-f71f-4091-9239-d9a520f83361');\n",
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
              "<div id=\"df-d1bbcebb-7a89-4585-b090-1f8b107be7cb\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-d1bbcebb-7a89-4585-b090-1f8b107be7cb')\"\n",
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
              "        document.querySelector('#df-d1bbcebb-7a89-4585-b090-1f8b107be7cb button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OiZOiaRHsaYn",
        "outputId": "ab801e6e-4e6a-4fb4-8587-bb9e0db03b03"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 113036 entries, 0 to 113035\n",
            "Data columns (total 18 columns):\n",
            " #   Column            Non-Null Count   Dtype \n",
            "---  ------            --------------   ----- \n",
            " 0   Date              113036 non-null  object\n",
            " 1   Day               113036 non-null  int64 \n",
            " 2   Month             113036 non-null  object\n",
            " 3   Year              113036 non-null  int64 \n",
            " 4   Customer_Age      113036 non-null  int64 \n",
            " 5   Age_Group         113036 non-null  object\n",
            " 6   Customer_Gender   113036 non-null  object\n",
            " 7   Country           113036 non-null  object\n",
            " 8   State             113036 non-null  object\n",
            " 9   Product_Category  113036 non-null  object\n",
            " 10  Sub_Category      113036 non-null  object\n",
            " 11  Product           113036 non-null  object\n",
            " 12  Order_Quantity    113036 non-null  int64 \n",
            " 13  Unit_Cost         113036 non-null  int64 \n",
            " 14  Unit_Price        113036 non-null  int64 \n",
            " 15  Profit            113036 non-null  int64 \n",
            " 16  Cost              113036 non-null  int64 \n",
            " 17  Revenue           113036 non-null  int64 \n",
            "dtypes: int64(9), object(9)\n",
            "memory usage: 15.5+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " Preprocessing"
      ],
      "metadata": {
        "id": "K-ax8yIIxeXK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class  preprocessing:\n",
        "    def __init__(self, df):\n",
        "        self.df = df\n",
        "\n",
        "    def Visualization(self):\n",
        "        plt.figure(figsize=(3, 3))\n",
        "        plt.imshow(self.df.isnull(), cmap='viridis', aspect='auto', interpolation='nearest')\n",
        "        plt.title('Null Values Visualization')\n",
        "        plt.xlabel('Columns')\n",
        "        plt.ylabel('Rows')\n",
        "        plt.colorbar()\n",
        "        plt.show()\n",
        "        self.df.isnull()\n",
        "        self.df.info()\n",
        "\n",
        "obj1 = preprocessing(df)\n",
        "obj1.Visualization()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 767
        },
        "id": "fDtJy3YDdLoF",
        "outputId": "8a655950-edc7-460d-cb4c-8e1e67233326"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 300x300 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 113036 entries, 0 to 113035\n",
            "Data columns (total 18 columns):\n",
            " #   Column            Non-Null Count   Dtype \n",
            "---  ------            --------------   ----- \n",
            " 0   Date              113036 non-null  object\n",
            " 1   Day               113036 non-null  int64 \n",
            " 2   Month             113036 non-null  object\n",
            " 3   Year              113036 non-null  int64 \n",
            " 4   Customer_Age      113036 non-null  int64 \n",
            " 5   Age_Group         113036 non-null  object\n",
            " 6   Customer_Gender   113036 non-null  object\n",
            " 7   Country           113036 non-null  object\n",
            " 8   State             113036 non-null  object\n",
            " 9   Product_Category  113036 non-null  object\n",
            " 10  Sub_Category      113036 non-null  object\n",
            " 11  Product           113036 non-null  object\n",
            " 12  Order_Quantity    113036 non-null  int64 \n",
            " 13  Unit_Cost         113036 non-null  int64 \n",
            " 14  Unit_Price        113036 non-null  int64 \n",
            " 15  Profit            113036 non-null  int64 \n",
            " 16  Cost              113036 non-null  int64 \n",
            " 17  Revenue           113036 non-null  int64 \n",
            "dtypes: int64(9), object(9)\n",
            "memory usage: 15.5+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate summary statistics (mean, median, etc.) for numeric columns"
      ],
      "metadata": {
        "id": "VqZRJZpQldqY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Calculate summary statistics (mean, median, etc.) for numeric columns\n",
        "class colums:\n",
        "    def __init__(self, df):\n",
        "        self.df = df\n",
        "    def numeric (self):\n",
        "      numeric_colums = self.df.select_dtypes(include=['number'])\n",
        "      print(numeric_colums.head())\n",
        "\n",
        "obj2 = colums(df)\n",
        "obj2.numeric()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RM3ShqPsec31",
        "outputId": "609224aa-9825-4253-c619-c5acd385cc9e"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Day  Year  Customer_Age  Order_Quantity  Unit_Cost  Unit_Price  Profit  \\\n",
            "0   26  2013            19               8         45         120     590   \n",
            "1   26  2015            19               8         45         120     590   \n",
            "2   23  2014            49              23         45         120    1366   \n",
            "3   23  2016            49              20         45         120    1188   \n",
            "4   15  2014            47               4         45         120     238   \n",
            "\n",
            "   Cost  Revenue  \n",
            "0   360      950  \n",
            "1   360      950  \n",
            "2  1035     2401  \n",
            "3   900     2088  \n",
            "4   180      418  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class summary_statistics:\n",
        "  def __init__(self, df):\n",
        "    self.df = df\n",
        "  def mean_median_mode(self):\n",
        "    numeric_colums = self.df.select_dtypes(include=['number'])\n",
        "    column = numeric_colums.iloc[:, 2:]\n",
        "    mean_value = column.mean()\n",
        "    median_value = column.median()\n",
        "    mode_value = column.mode()\n",
        "    print(f\"Mean : {mean_value}\")\n",
        "    print(f\"Median : {median_value}\")\n",
        "    print(f\"Mode : {mode_value}\")\n",
        "obj3 = summary_statistics(df)\n",
        "obj3.mean_median_mode()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qC2ae49lhklg",
        "outputId": "6a6fc245-a6e9-482e-a7e9-125852dd8e8b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mean : Customer_Age       35.919212\n",
            "Order_Quantity     11.901660\n",
            "Unit_Cost         267.296366\n",
            "Unit_Price        452.938427\n",
            "Profit            285.051665\n",
            "Cost              469.318695\n",
            "Revenue           754.370360\n",
            "dtype: float64\n",
            "Median : Customer_Age       35.0\n",
            "Order_Quantity     10.0\n",
            "Unit_Cost           9.0\n",
            "Unit_Price         24.0\n",
            "Profit            101.0\n",
            "Cost              108.0\n",
            "Revenue           223.0\n",
            "dtype: float64\n",
            "Mode :    Customer_Age  Order_Quantity  Unit_Cost  Unit_Price  Profit  Cost  Revenue\n",
            "0            31               1          2           5       3  1252       35\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Find the total number of Product_Category, Sub_Category, Product"
      ],
      "metadata": {
        "id": "z_Aw6EP31AX3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Total unique values\n",
        "class unique_values:\n",
        "  def unique(self):\n",
        "    total_product_categories = df['Product_Category'].nunique()\n",
        "    total_sub_categories = df['Sub_Category'].nunique()\n",
        "    total_products = df['Product'].nunique()\n",
        "\n",
        "    print(f\"Total Product Categories: {total_product_categories}\")\n",
        "    print(f\"Total Sub Categories: {total_sub_categories}\")\n",
        "    print(f\"Total Products: {total_products}\")\n",
        "\n",
        "obj4 = unique_values()\n",
        "obj4.unique()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mmqiyUKfy_si",
        "outputId": "e0e7411f-577a-481f-913c-e3b76ef122c2"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Product Categories: 3\n",
            "Total Sub Categories: 17\n",
            "Total Products: 130\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " Histogram for  Customer_Age"
      ],
      "metadata": {
        "id": "Q6RebTGpqlun"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class histogram:\n",
        "  def __init__(self, df):\n",
        "    self.df = df\n",
        "  def hist(self):\n",
        "    df['Customer_Age'].hist(bins=10000, color='blue', edgecolor='black')\n",
        "    plt.title(\" Customer Age\")\n",
        "    plt.xlabel(\"age\")\n",
        "    plt.ylabel(\"No.of people\")\n",
        "    plt.show()\n",
        "\n",
        "obj5 = histogram(df)\n",
        "obj5.hist()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "Q5d55I3Sqjui",
        "outputId": "43e864ca-419f-4b8a-96b9-2192ffc82532"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ZwxJxvvvv28z/uuvvxoDBw40/Pz8DDc3N6NatWpGt27djK+//to6J+sWAPv27fvTfTlz5kxDkrF58+a7zlm0aJEhyfjuu+8MwzCMW7duGW+++abh5+dneHl5GY8//rhx4sQJo0KFCsbw4cNt1r1y5YoRHh5uBAYGGu7u7kbFihWNNm3aGB988IGRlpb2p/UBzs7FMP7/lYkAgCIpKSlJ5cqV09tvv23zlieA+8M1SQBQhNy4cSPbWNY1Wfn1BcOAs+KaJAAoQlasWKFFixapa9euKl26tHbs2KHly5erc+fOObq3FICcIyQBQBHSuHFjlSxZUjNmzFBKSor1Yu63337b0aUBxQ7XJAEAAJjgmiQAAAAThCQAAAATXJOUA5mZmTp//rzKlClj9/cnAQAAxzAMQ1euXFHVqlXl6mr/eSFCUg6cP38+R1/oCQAACp9z586pevXqdq9HSMqBrK9GOHfunHx8fBxczd2lp6dr06ZN6ty5s9zc3BxdjkM4+z5w9v4l9gH9O3f/Evvg9v5v3LihGjVqWP8etxchKQey3mLz8fEp9CHJ29tbPj4+TvmLIbEPnL1/iX1A/87dv8Q+MOs/t5fKcOE2AACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISAACACUISnILFYlFERIQsFoujSwEAFBGEJDgFi8WiyMhIQhIAIMcISQAAACYISQAAACYISQAAACYISQAAACYISYCd+KQcADgHQhJgJz4pBwDOgZAEAABggpAEAABggpAEAABggpAEAABggpAEAABggpCEIoeP4AMACgIhCUUOH8EHABQEQhIAAIAJQhIAAIAJQhIAAIAJQhIAAIAJQhIAAIAJQhIAAIAJQhIAAIAJQhIAAIAJQhKcHnfwBgCYISTB6XEHbwCAGUISAACAiUITkt577z25uLho9OjR1rGbN28qLCxMFSpUUOnSpdW7d28lJibarBcfH6/Q0FB5e3urUqVKGjdunG7dumUzZ+vWrWrevLk8PDwUGBioRYsWFUBHAACgKCsUIWnfvn2aP3++GjdubDM+ZswYrV27VqtWrdK2bdt0/vx59erVy7o8IyNDoaGhSktL065du7R48WItWrRIkydPts45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JGnWrFlydXVV7969lZqaqpCQEM2dO9c6t0SJElq3bp1eeeUVBQUFqVSpUho0aJDeeust65yAgACtX79eY8aM0ezZs1W9enV9/vnnxerj/wAAIG/ZHZIsFovatGmTbbxNmzayWCx2bSsnH6zz9PTUnDlzNGfOnLvO8ff314YNG+65nQ4dOujQoUN21QcAAJyX3dckBQYGauXKldnGV6xYoQcffDBPigLgPCwWiyIiIuz+RxYA5De7zyRFRkaqX79+2r59u/WapJ07d2rz5s2m4QkA7sVisSgyMlI9evRQlSpVHF0OAFjZfSapd+/e2rNnjypWrKg1a9ZozZo1qlixovbu3aunn346P2oEAAAocLm6T1KLFi20ZMmSvK4FAACg0MjVfZIAAACKuxyfSXJ1df3TO2u7uLjc990tAQAACoMch6TVq1ffdVlMTIw++ugj6zeQAwAAFHU5Dkk9e/bMNhYXF6eJEydq7dq1GjBggM0NHAEAAIqyXF2TdP78eb344otq1KiRbt26pdjYWC1evFj+/v55XR8AAIBD2BWSkpOTNWHCBAUGBurYsWPavHmz1q5dq4YNG+ZXfQCcGDeaBOBIOQ5JM2bMUO3atbVu3TotX75cu3bt0qOPPpqftQFwclk3miQkAXCEHF+TNHHiRHl5eSkwMFCLFy/W4sWLTed9++23eVYcAJixWCyaP3++Xn755Wx36U5MTLT+rF69uiPKA1BM5DgkDRw48E9vAYC8c6+/BABnd6+vMklISLD+JCQBuB85DkmLFi3KxzJwJ77PCgAAx+KO2wAAACYISQAAACYISQAAACYISQAAACYISQAAACYISQAAACYISQAAACYISQAAACYISQCcAl+WC8BehCQAToEvywVgL0ISAACACUISAACACUISAACACUISANwFF3sDzo2QBAB3wcXegHMjJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAFwahaLRREREbJYLI4uBUAhQ0gC4NQsFosiIyMJSQCyISQBAACYICQBAACYICQBAACYICQBAACYICQ5GJ+sAQCgcCIkORifrAEAoHAiJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEAAJggJAEA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R2zWP3z4sH766SeVLl3a+qhXr54k2bxtB6D4KunoAgAgP3Tv3l3+/v767LPPVLVqVWVmZqphw4ZKS0vL0fpXr15V9+7dNX369GzLqlSpktflAiiECEkAip1Lly4pLi5On332mR599FFJ0o4dO6zLH3roIS1ZskSpqany8PCQJO3bt89mG82bN9c333yjWrVqqWRJ/lcJOCPebgNQ7JQrV04VKlTQp59+ql9++UVbtmzR2LFjrcv79++vzMxMvfTSSzpx4oSioqL0wQcfSJJcXFwkSWFhYbp8+bKeffZZ7du3T7/++quioqI0ePBgZWRkOKQvAAWLkASg2HF1ddVXX32lAwcOqGHDhhozZozef/9963IfHx+tXbtWsbGxatq0qSZNmqTJkydLkvU6papVq2rnzp3KyMhQ586d1ahRI40ePVply5aVqyv/6wScAZ9uAwBJS5cu1eDBg5WcnCwvLy9HlwOgEOCNdgBO6csvv1Tt2rVVrVo1HT58WBMmTFDfvn0JSACsCEkAnFJCQoImT56shIQEValSRX/96181bdo0R5cFoBDh7TYAAAATXH0IAABggpAEAABggpAEAABggpAEAABggpAEAABggpAEAABggpAEAABggpAEAABggpAEAABg4v8BJys7GbyMTLsAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Revenue distribution\n"
      ],
      "metadata": {
        "id": "VwMxK7fQxGeS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "visualise gender distribution\n"
      ],
      "metadata": {
        "id": "UUeu1GQcLtQD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class sgender_distribution:\n",
        "  def gender (self):\n",
        "    gender_counts = df['Customer_Gender'].value_counts()\n",
        "    print('Gender Counts')\n",
        "    print(gender_counts)\n",
        "    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.0f%%')\n",
        "    plt.title('Customer Gender Distribution')\n",
        "    plt.show()\n",
        "\n",
        "obj6 = sgender_distribution()\n",
        "obj6.gender()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 515
        },
        "id": "36k9nRqYJBJ_",
        "outputId": "9dbfa469-5295-4602-f06f-f838ee335808"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gender Counts\n",
            "Customer_Gender\n",
            "M    58312\n",
            "F    54724\n",
            "Name: count, dtype: int64\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ya5/ozsALXpyiAnyKiwFUo+iDFc55KS6/s2t/DcNsBXLTudiiT47428FRJxXABFJvJYxqQJLgbShKPNcURRnuobnsJW4ysJWAlRc8P35X86Kqs+nN7lm4kY/1zkAZotr275/KOAfdvb/Z/+1RJ0rAV6MhlSOpUBkt7nKQghXCZgCeBYw+SyWAhERKXgVbiIiUrAUiIhIwVIgIiIFS4GIiBQsBSIiUrAUiIhIwVIgIiIFS4GIiBQsBaI6SElJgU6nq/J15IgPjexKmmaUHYBIbW688UYsWLDA7baoqChJaYg8i6VAVEd+fn5o1qyZ7BhEDYKbj4iISMFSIKqjb7/9FkFBQcrX7bffLjsSkcdw8xFRHV133XWYO3eu8r3FYpGYhsizWApEdWSxWJCcnCw7BlGD4OYjIiJSsBSIiEjBUiAiIgUvx0lERAquKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQERECpYCEREpWApERKRgKRARkYKlQEREiv8HztDsPVVxu+oAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Relationship between Age Group and Revenue."
      ],
      "metadata": {
        "id": "UalfQvC76Kgm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class relationship:\n",
        "  def bar (self):\n",
        "    plt.bar(df['Age_Group'], df['Revenue'], width=0.8, color=None, label=None, align='center')\n",
        "    plt.xlabel('Age Group')\n",
        "    plt.ylabel('Revenue')\n",
        "    plt.title('Relationship between Age and Revenue.')\n",
        "    plt.legend()\n",
        "    plt.show()\n",
        "obj7 = relationship()\n",
        "obj7.bar()"
      ],
      "metadata": {
        "id": "f0sfMrWML1s0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 489
        },
        "outputId": "a3878f26-08f0-409d-c813-abc0986c4b3e"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:matplotlib.legend:No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHHCAYAAACiOWx7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABjPUlEQVR4nO3dd1gU5/428HtpCwIL0lERFRSxKypiiRrRVTEJtqhRg70c1EROLByNqInRaIxoLNjRWFFjiTUee8GGgh1L4GADbIAVBJ73D9+dnyPFAdFFc3+ua6+LnfnOzDNtuXfaqoQQAkRERESULwN9N4CIiIjoQ8DQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0EQfvf3790OlUmH//v1FOl6VSoXx48cX6TgLKj4+HiqVCr/88ssba8ePHw+VSlVk09Yt1/Xr1xfZOOnjpttew8PD9d0UokJhaKJiJTw8HCqVSnoZGRmhdOnS6NWrF27duvXe27N9+3a9B6N/kqNHj2L8+PFISUnRd1PeuZSUFJiamkKlUuHSpUv6bk6xogvkupehoSEcHBzQqVMnLivSK4YmKpYmTpyI33//HWFhYWjTpg1WrFiBpk2b4vnz5++1Hdu3b8eECRNy7ffs2TOMHTv2vbbnbYwdOxbPnj3TdzPydfToUUyYMOEfEZrWrVsHlUoFJycnrFy5Ut/NKZaGDRuG33//HYsWLUL37t2xbds2NGnSBImJifpuGv1DGem7AUS5adOmDerWrQsA6NevH+zs7PDzzz9jy5Yt+PLLL/XcupdMTU313YQCMTIygpERd/niYsWKFWjbti1cXV2xatUq/Pjjj/puUrHTpEkTdOrUSXrv4eGBwYMHY/ny5Rg5cqQeW0b/VDzSRB+EJk2aAACuX78u63758mV06tQJNjY2MDU1Rd26dbFly5Y3ju/QoUPo3LkzypYtC7VaDRcXFwwfPlx2JKZXr16YM2cOAMhOFejkdk3TmTNn0KZNG2g0GlhYWKBFixY4duyYrEZ3CvLIkSMICgqCvb09zM3N0b59e9y9e1dWe+rUKWi1WtjZ2cHMzAzly5dHnz59cp2nBQsWwM3NDWq1GvXq1cPJkydl/XO7pkmlUmHIkCFYuXIlPDw8YGpqCi8vLxw8ePCNy1AnKysL//nPf+Dk5ARzc3N8/vnnuHHjRo6648ePo3Xr1rCyskKJEiXQtGlTHDlyRNa+ESNGAADKly8vLe/4+Hh06NABderUkY3vs88+g0qlkq3v48ePQ6VSYceOHVK3lJQUfPvtt3BxcYFarYa7uzt+/vlnZGdny8aXnZ2N0NBQVK1aFaampnB0dMTAgQPx8OFDWV25cuXQrl07HD58GPXr14epqSkqVKiA5cuXK15mCQkJOHToELp27YquXbsiLi4OR48ezbV2zpw5qFChAszMzFC/fn0cOnQIzZo1Q7NmzWR16enpCAkJgbu7u7RNjxw5Eunp6W9sj5L9AXi5T1hYWODWrVvw9/eHhYUF7O3t8d133yErK0tWm5KSgl69esHKygrW1tYICAh46yOIeX0O3Lp1C3369IGjoyPUajWqVq2KJUuWSP2TkpJgZGSU61Hj2NhYqFQqzJ49W9b2N20zr15P+KZ9L7f1BbxcnuXKlZN1U7odkn7wayd9EOLj4wEAJUuWlLpduHABjRo1QunSpTF69GiYm5sjIiIC/v7+2LBhA9q3b5/n+NatW4enT59i8ODBsLW1xYkTJ/Dbb7/h5s2bWLduHQBg4MCBuH37Nnbv3o3ff//9jW28cOECmjRpAo1Gg5EjR8LY2Bjz589Hs2bNcODAAXh7e8vqhw4dipIlSyIkJATx8fEIDQ3FkCFDsHbtWgBAcnIyWrVqBXt7e4wePRrW1taIj4/HH3/8kWPaq1atwqNHjzBw4ECoVCpMnToVHTp0wN9//w1jY+N8233gwAGsXbsWw4YNg1qtxty5c9G6dWucOHEC1apVe+N8T5o0CSqVCqNGjUJycjJCQ0Ph6+uL6OhomJmZAQD27t2LNm3awMvLCyEhITAwMMDSpUvx6aef4tChQ6hfvz46dOiAK1euYPXq1ZgxYwbs7OwAAPb29mjSpAk2b96MtLQ0aDQaCCFw5MgRGBgY4NChQ/j8888BvPznb2BggEaNGgEAnj59iqZNm+LWrVsYOHAgypYti6NHjyI4OBh37txBaGioNB8DBw5EeHg4evfujWHDhiEuLg6zZ8/GmTNncOTIEdlyvHbtGjp16oS+ffsiICAAS5YsQa9eveDl5YWqVau+cZmtXr0a5ubmaNeuHczMzODm5oaVK1eiYcOGsrp58+ZhyJAhaNKkCYYPH474+Hj4+/ujZMmSKFOmjFSXnZ2Nzz//HIcPH8aAAQPg6emJc+fOYcaMGbhy5Qo2bdqUb3uU7A86WVlZ0Gq18Pb2xi+//IL//ve/mD59Otzc3DB48GAAgBACX3zxBQ4fPoxBgwbB09MTGzduREBAwBuXTX5y+xxISkpCgwYNpC8A9vb22LFjB/r27Yu0tDR8++23cHR0RNOmTREREYGQkBDZONeuXQtDQ0N07twZQMG2GeDt9r3cFGQ7JD0QRMXI0qVLBQDx3//+V9y9e1fcuHFDrF+/Xtjb2wu1Wi1u3Lgh1bZo0UJUr15dPH/+XOqWnZ0tGjZsKCpWrCh127dvnwAg9u3bJ3V7+vRpjmlPnjxZqFQq8b///U/qFhgYKPLaTQCIkJAQ6b2/v78wMTER169fl7rdvn1bWFpaik8++STHPPr6+ors7Gyp+/Dhw4WhoaFISUkRQgixceNGAUCcPHkyz+UVFxcnAAhbW1vx4MEDqfvmzZsFAPHnn39K3UJCQnLMCwABQJw6dUrq9r///U+YmpqK9u3b5zldIf5vuZYuXVqkpaVJ3SMiIgQAMXPmTCHEy3VSsWJFodVqZfP79OlTUb58edGyZUup27Rp0wQAERcXJ5vWyZMnBQCxfft2IYQQZ8+eFQBE586dhbe3t1T3+eefi9q1a0vvf/jhB2Fubi6uXLkiG9/o0aOFoaGhSEhIEEIIcejQIQFArFy5Ula3c+fOHN1dXV0FAHHw4EGpW3JyslCr1eLf//53vstMp3r16qJ79+7S+//85z/Czs5OvHjxQuqWnp4ubG1tRb169WTdw8PDBQDRtGlTqdvvv/8uDAwMxKFDh2TTCQsLEwDEkSNH8m2P0v0hICBAABATJ06U1dauXVt4eXlJ7zdt2iQAiKlTp0rdMjMzRZMmTQQAsXTp0nzbo9u2lixZIu7evStu374tdu7cKdzd3YVKpRInTpyQavv27SucnZ3FvXv3ZOPo2rWrsLKykuZt/vz5AoA4d+6crK5KlSri008/ld4r3WYKsu81bdpUtr50AgIChKurq/S+INsh6QdPz1Gx5OvrC3t7e7i4uKBTp04wNzfHli1bpG/XDx48wN69e/Hll1/i0aNHuHfvHu7du4f79+9Dq9Xi6tWr+d5tpzsCAgBPnjzBvXv30LBhQwghcObMmQK3NysrC3/99Rf8/f1RoUIFqbuzszO++uorHD58GGlpabJhBgwYIDtd1qRJE2RlZeF///sfAMDa2hoAsHXrVrx48SLf6Xfp0kX27Vt3GuPvv/9+Y9t9fHzg5eUlvS9btiy++OIL7Nq1K8cpl9x8/fXXsLS0lN536tQJzs7O2L59OwAgOjoaV69exVdffYX79+9L6+rJkydo0aIFDh48mONU2etq164NCwsL6bThoUOHUKZMGXz99dc4ffo0nj59CiEEDh8+LM078PIISpMmTVCyZElpuvfu3YOvry+ysrKk8a1btw5WVlZo2bKlrM7LywsWFhbYt2+frD1VqlSRTcfe3h4eHh6KlvfZs2dx7tw5dOvWTerWrVs33Lt3D7t27ZK6nTp1Cvfv30f//v1l16J1795dtq517ff09ETlypVl7f/0008BIEf7X1fQ/WHQoEGy902aNJHN+/bt22FkZCQdeQIAQ0NDDB06NN92vK5Pnz6wt7dHqVKl0Lp1a6SmpuL3339HvXr1ALw8orVhwwZ89tlnEELI5l2r1SI1NRWnT58GAHTo0AFGRkbSkVwAOH/+PC5evIguXbpI3ZRuMzpvs++9rqDbIb1/PD1HxdKcOXNQqVIlpKamYsmSJTh48CDUarXU/9q1axBC4Pvvv8f333+f6ziSk5NRunTpXPslJCRg3Lhx2LJlS45rBVJTUwvc3rt37+Lp06fw8PDI0c/T0xPZ2dm4ceOG7NRN2bJlZXW6D15de5o2bYqOHTtiwoQJmDFjBpo1awZ/f3989dVXsmWhZFz5qVixYo5ulSpVwtOnT3H37l04OTkVaHiVSgV3d3fpVMrVq1cBIN9TM6mpqTmCwKsMDQ3h4+ODQ4cOAXgZmpo0aYLGjRsjKysLx44dg6OjIx48eCALM1evXsXZs2dhb2+f63iTk5OlutTUVDg4OORbp/P68gZeLnMly3vFihUwNzdHhQoVcO3aNQAvbyooV64cVq5cCT8/PwCQwrO7u7tseCMjoxzXwVy9ehWXLl1643zmpSD7g6mpaY7pvD7v//vf/+Ds7AwLCwtZXW77R37GjRuHJk2a4PHjx9i4cSPWrFkDA4P/+65/9+5dpKSkYMGCBViwYEGu49DNu52dHVq0aIGIiAj88MMPAF6emjMyMkKHDh2keqXbjM7b7HuvK+h2SO8fQxMVS/Xr15funvP390fjxo3x1VdfITY2FhYWFtKRie+++w5arTbXcbz+z0YnKysLLVu2xIMHDzBq1ChUrlwZ5ubmuHXrFnr16vXGox5FxdDQMNfuQggAkB4ceezYMfz555/YtWsX+vTpg+nTp+PYsWOyf0hvGpc+6ZbntGnTUKtWrVxrXv/nmpvGjRtj0qRJeP78OQ4dOoQxY8bA2toa1apVw6FDh+Do6AgAstCUnZ2Nli1b5nmnVaVKlaQ6BweHPG/9f/0faGGXtxACq1evxpMnT1ClSpUc/ZOTk/H48WNFy+NV2dnZqF69On799ddc+7u4uOQ5bEH3h7zm/V2oXr06fH19Abz8HHj69Cn69++Pxo0bw8XFRWpbjx498gzlNWrUkP7u2rUrevfujejoaNSqVQsRERFo0aKFdP0coHyb0VGyLahUqly3jdeP5BZ0O6T3j6GJij1DQ0NMnjwZzZs3x+zZszF69GjpFJixsbH0oarUuXPncOXKFSxbtgxff/211H337t05apU+Qdve3h4lSpRAbGxsjn6XL1+GgYFBvv+48tOgQQM0aNAAkyZNwqpVq9C9e3esWbMG/fr1K9T4Xqc7EvSqK1euoESJEoo+pF8fXgiBa9euSf+s3NzcAAAajeaN6yq/5d2kSRNkZGRg9erVuHXrlhSOPvnkEyk0VapUSQpPumk/fvz4jdN1c3PDf//7XzRq1Eh2qqqoHThwADdv3sTEiRPh6ekp6/fw4UMMGDAAmzZtQo8ePeDq6grg5VHV5s2bS3WZmZmIj4+XhQE3NzfExMSgRYsWBX7qe0H2B6VcXV2xZ8+eHAEwt/2jIKZMmYKNGzdi0qRJCAsLg729PSwtLZGVlaXoc8Df3x8DBw6UTtFduXIFwcHBshql20xBlCxZMtfTdbqjia9O+31sh1R4vKaJPgjNmjVD/fr1ERoaiufPn8PBwQHNmjXD/PnzcefOnRz1r9+6/yrdN8NXv/kJITBz5swctebm5gDwxlulDQ0N0apVK2zevFk6LQW8vLNn1apVaNy4MTQaTb7jeN3Dhw9zfDvVHalRchu5UpGRkdJ1HwBw48YNbN68Ga1atVJ0VGH58uV49OiR9H79+vW4c+cO2rRpAwDw8vKCm5sbfvnlFzx+/DjH8K+uq/yWt7e3N4yNjfHzzz/DxsZGOtXZpEkTHDt2DAcOHJAdZQKAL7/8EpGRkbJrhXRSUlKQmZkp1WVlZUmnbV6VmZlZZA/b1J2aGzFiBDp16iR79e/fHxUrVpSOMtStWxe2trZYuHCh1E4AWLlyZY5TP19++SVu3bqFhQsX5pjms2fP8OTJkzzbVJD9Qam2bdsiMzMT8+bNk7plZWXht99+K/Q4gZehomPHjggPD0diYiIMDQ3RsWNHbNiwAefPn89R//rngLW1NbRaLSIiIrBmzRqYmJjA399fVqN0mylouy9fvixrT0xMjOyRG7ppK90O79y5g8uXL7/xekcqWjzSRB+MESNGoHPnzggPD8egQYMwZ84cNG7cGNWrV0f//v1RoUIFJCUlITIyEjdv3kRMTEyu46lcuTLc3Nzw3Xff4datW9BoNNiwYUOu1yDoLpAeNmwYtFotDA0N0bVr11zH++OPP2L37t1o3Lgx/vWvf8HIyAjz589Heno6pk6dWuD5XbZsGebOnYv27dvDzc0Njx49wsKFC6HRaNC2bdsCjy8v1apVg1arlT1yAECeT0J/nY2NDRo3bozevXsjKSkJoaGhcHd3R//+/QEABgYGWLRoEdq0aYOqVauid+/eKF26NG7duoV9+/ZBo9Hgzz//BPB/y3vMmDHo2rUrjI2N8dlnn8Hc3BwlSpSAl5cXjh07Jj2jCXh5pOnJkyd48uRJjtA0YsQIbNmyBe3atZMeCfDkyROcO3cO69evR3x8POzs7NC0aVMMHDgQkydPRnR0NFq1agVjY2NcvXoV69atw8yZM2UPWSyM9PR0bNiwAS1btszzwaiff/45Zs6cieTkZDg4OGD8+PEYOnQoPv30U3z55ZeIj49HeHg43NzcZEeUevbsiYiICAwaNAj79u1Do0aNkJWVhcuXLyMiIgK7du2STne/riD7g1KfffYZGjVqhNGjRyM+Ph5VqlTBH3/8UajrBV83YsQIREREIDQ0FFOmTMGUKVOwb98+eHt7o3///qhSpQoePHiA06dP47///S8ePHggG75Lly7o0aMH5s6dC61WK91w8er4lWwzBdGnTx/8+uuv0Gq16Nu3L5KTkxEWFoaqVavKbhApyHYYHByMZcuWIS4uLsc1bvQOve/b9Yjyo7sdP7fb7LOysoSbm5twc3MTmZmZQgghrl+/Lr7++mvh5OQkjI2NRenSpUW7du3E+vXrpeFye+TAxYsXha+vr7CwsBB2dnaif//+IiYmJsft0JmZmWLo0KHC3t5eqFQq2S37eO2RA0IIcfr0aaHVaoWFhYUoUaKEaN68uTh69KiieXy9nadPnxbdunUTZcuWFWq1Wjg4OIh27drJHg+gu+152rRpOZbX6+3L65EDgYGBYsWKFaJixYpCrVaL2rVry5ZVXnTtXb16tQgODhYODg7CzMxM+Pn5yW5T1zlz5ozo0KGDsLW1FWq1Wri6uoovv/xS7NmzR1b3ww8/iNKlSwsDA4Mcjx8YMWKEACB+/vln2TDu7u4CgOxxDzqPHj0SwcHBwt3dXZiYmAg7OzvRsGFD8csvv4iMjAxZ7YIFC4SXl5cwMzMTlpaWonr16mLkyJHi9u3bUo2rq6vw8/PLMZ28bivX2bBhgwAgFi9enGfN/v37ZY9rEEKIWbNmCVdXV6FWq0X9+vXFkSNHhJeXl2jdurVs2IyMDPHzzz+LqlWrCrVaLUqWLCm8vLzEhAkTRGpqap7TFEL5/hAQECDMzc1zDJ/btnX//n3Rs2dPodFohJWVlejZs6c4c+ZMgR45sG7dulz7N2vWTGg0GunxHElJSSIwMFC4uLgIY2Nj4eTkJFq0aCEWLFiQY9i0tDRhZmYmAIgVK1bkOn4l20xB9j0hhFixYoWoUKGCMDExEbVq1RK7du3K8cgBHSXboe7xD68/noPeLZUQxeBKUSLSC5VKhcDAQNnTkKl4y87Ohr29PTp06JDr6Tgiend4TRMRUTH1/PnzHNe1LV++HA8ePMj1ZzmI6N3iNU1ERMXUsWPHMHz4cHTu3Bm2trY4ffo0Fi9ejGrVqkk/+0FE7w9DExFRMVWuXDm4uLhg1qxZePDgAWxsbPD1119jypQpMDEx0XfziP5xeE0TERERkQK8pomIiIhIAYYmIiIiIgV4TVMRyc7Oxu3bt2FpaVngnzEgIiIi/RBC4NGjRyhVqpTsB6Fzw9BURG7fvl3o3xYjIiIi/bpx4wbKlCmTbw1DUxGxtLQE8HKhF/Q3xoiIiEg/0tLS4OLiIv0fz5c+H0cuhBA3b94U3bt3FzY2NsLU1FRUq1ZN9vMS2dnZ4vvvvxdOTk7C1NRUtGjRQly5ckU2jvv374uvvvpKWFpaCisrK9GnTx/x6NEjWU1MTIxo3LixUKvVokyZMjl+hkEIISIiIoSHh4dQq9WiWrVqYtu2bYrnIzU1VQB4488VEBERUfFRkP/fer0Q/OHDh2jUqBGMjY2xY8cOXLx4EdOnT0fJkiWlmqlTp2LWrFkICwvD8ePHYW5uDq1Wi+fPn0s13bt3x4ULF7B7925s3boVBw8exIABA6T+aWlpaNWqFVxdXREVFYVp06Zh/PjxWLBggVRz9OhRdOvWDX379sWZM2fg7+8Pf3//XH85m4iIiP6B3kOIy9OoUaNE48aN8+yfnZ0tnJycZD+ImJKSItRqtVi9erUQ4uUPTeK1Hz/dsWOHUKlU4tatW0IIIebOnStKliwp0tPTZdP28PCQ3n/55Zc5foTT29tbDBw4UNG88EgTERHRh+eDOdK0ZcsW1K1bF507d4aDgwNq164t+wHKuLg4JCYmwtfXV+pmZWUFb29vREZGAgAiIyNhbW2NunXrSjW+vr4wMDDA8ePHpZpPPvlE9gRdrVaL2NhYPHz4UKp5dTq6Gt10Xpeeno60tDTZi4iIiD5eeg1Nf//9N+bNm4eKFSti165dGDx4MIYNG4Zly5YBABITEwEAjo6OsuEcHR2lfomJiXBwcJD1NzIygo2Njawmt3G8Oo28anT9Xzd58mRYWVlJL945R0REpB9ZWVl4/vx5rq+srKwim45e757Lzs5G3bp18dNPPwEAateujfPnzyMsLAwBAQH6bNobBQcHIygoSHqvu/qeiIiI3g8hBBITE5GSkpJvnbW1NZycnN76OYp6DU3Ozs6oUqWKrJunpyc2bNgAAHBycgIAJCUlwdnZWapJSkpCrVq1pJrk5GTZODIzM/HgwQNpeCcnJyQlJclqdO/fVKPr/zq1Wg21Wq14XomIiKho6QKTg4MDSpQokSMUCSHw9OlTKSe8miUKQ6+n5xo1aoTY2FhZtytXrsDV1RUAUL58eTg5OWHPnj1S/7S0NBw/fhw+Pj4AAB8fH6SkpCAqKkqq2bt3L7Kzs+Ht7S3VHDx4EC9evJBqdu/eDQ8PD+lOPR8fH9l0dDW66RAREVHxkZWVJQUmW1tbmJmZwdTUVPYyMzODra0tHBwckJKS8van6t75Zen5OHHihDAyMhKTJk0SV69eFStXrhQlSpQQK1askGqmTJkirK2txebNm8XZs2fFF198IcqXLy+ePXsm1bRu3VrUrl1bHD9+XBw+fFhUrFhRdOvWTeqfkpIiHB0dRc+ePcX58+fFmjVrRIkSJcT8+fOlmiNHjggjIyPxyy+/iEuXLomQkBBhbGwszp07p2heePccERHR+/Ps2TNx8eJF8fTp0zfWPn36VFy8eFGWHXQK8v9b7w+3/PPPP0W1atWEWq0WlStXFgsWLJD11z3c0tHRUajVatGiRQsRGxsrq7l//77o1q2bsLCwEBqNRvTu3Tvfh1uWLl1aTJkyJUdbIiIiRKVKlYSJiYmoWrUqH25JRERUTOlCU25BqCC1Bfn/rRJCiLc/SEZpaWmwsrJCamoqf0aFiIjoHXv+/Dni4uJQvnx5mJqaFrq2IP+/9XpNExEREdGHgqGJiIiISAGGJiIiIvpgKbnKqKiuRGJoIiIiog+OsbExAODp06dvrNXV6IYpLL0+3JKIiIioMAwNDWFtbS09uPJND7e0traGoaHhW02ToYlIj8qN3qbvJvxjxU/x03cTiOgt6X614/VfBnmd7mdU3hZDExEREX2QVCoVnJ2d4eDgIPvVj1cZGxu/9REmHYYmIiIi+qAZGhoWWTDKDy8EJyIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUkCvoWn8+PFQqVSyV+XKlaX+z58/R2BgIGxtbWFhYYGOHTsiKSlJNo6EhAT4+fmhRIkScHBwwIgRI5CZmSmr2b9/P+rUqQO1Wg13d3eEh4fnaMucOXNQrlw5mJqawtvbGydOnHgn80xEREQfJr0faapatSru3LkjvQ4fPiz1Gz58OP7880+sW7cOBw4cwO3bt9GhQwepf1ZWFvz8/JCRkYGjR49i2bJlCA8Px7hx46SauLg4+Pn5oXnz5oiOjsa3336Lfv36YdeuXVLN2rVrERQUhJCQEJw+fRo1a9aEVqtFcnLy+1kIREREVOyphBBCXxMfP348Nm3ahOjo6Bz9UlNTYW9vj1WrVqFTp04AgMuXL8PT0xORkZFo0KABduzYgXbt2uH27dtwdHQEAISFhWHUqFG4e/cuTExMMGrUKGzbtg3nz5+Xxt21a1ekpKRg586dAABvb2/Uq1cPs2fPBgBkZ2fDxcUFQ4cOxejRoxXNS1paGqysrJCamgqNRvM2i4X+QcqN3qbvJvxjxU/x03cTiKgYKMj/b70fabp69SpKlSqFChUqoHv37khISAAAREVF4cWLF/D19ZVqK1eujLJlyyIyMhIAEBkZierVq0uBCQC0Wi3S0tJw4cIFqebVcehqdOPIyMhAVFSUrMbAwAC+vr5SDREREZGRPifu7e2N8PBweHh44M6dO5gwYQKaNGmC8+fPIzExESYmJrC2tpYN4+joiMTERABAYmKiLDDp+uv65VeTlpaGZ8+e4eHDh8jKysq15vLly3m2PT09Henp6dL7tLS0gs08ERERfVD0GpratGkj/V2jRg14e3vD1dUVERERMDMz02PL3mzy5MmYMGGCvptBRERE74neT8+9ytraGpUqVcK1a9fg5OSEjIwMpKSkyGqSkpLg5OQEAHBycspxN53u/ZtqNBoNzMzMYGdnB0NDw1xrdOPITXBwMFJTU6XXjRs3CjXPRERE9GEoVqHp8ePHuH79OpydneHl5QVjY2Ps2bNH6h8bG4uEhAT4+PgAAHx8fHDu3DnZXW67d++GRqNBlSpVpJpXx6Gr0Y3DxMQEXl5esprs7Gzs2bNHqsmNWq2GRqORvYiIiOjjpdfQ9N133+HAgQOIj4/H0aNH0b59exgaGqJbt26wsrJC3759ERQUhH379iEqKgq9e/eGj48PGjRoAABo1aoVqlSpgp49eyImJga7du3C2LFjERgYCLVaDQAYNGgQ/v77b4wcORKXL1/G3LlzERERgeHDh0vtCAoKwsKFC7Fs2TJcunQJgwcPxpMnT9C7d2+9LBciIiIqfvR6TdPNmzfRrVs33L9/H/b29mjcuDGOHTsGe3t7AMCMGTNgYGCAjh07Ij09HVqtFnPnzpWGNzQ0xNatWzF48GD4+PjA3NwcAQEBmDhxolRTvnx5bNu2DcOHD8fMmTNRpkwZLFq0CFqtVqrp0qUL7t69i3HjxiExMRG1atXCzp07c1wcTkRERP9cen1O08eEz2miwuBzmvSHz2kiIuADe04TERER0YeAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIgWITmqZMmQKVSoVvv/1W6vb8+XMEBgbC1tYWFhYW6NixI5KSkmTDJSQkwM/PDyVKlICDgwNGjBiBzMxMWc3+/ftRp04dqNVquLu7Izw8PMf058yZg3LlysHU1BTe3t44ceLEu5hNIiIi+kAVi9B08uRJzJ8/HzVq1JB1Hz58OP7880+sW7cOBw4cwO3bt9GhQwepf1ZWFvz8/JCRkYGjR49i2bJlCA8Px7hx46SauLg4+Pn5oXnz5oiOjsa3336Lfv36YdeuXVLN2rVrERQUhJCQEJw+fRo1a9aEVqtFcnLyu595IiIi+iCohBBCnw14/Pgx6tSpg7lz5+LHH39ErVq1EBoaitTUVNjb22PVqlXo1KkTAODy5cvw9PREZGQkGjRogB07dqBdu3a4ffs2HB0dAQBhYWEYNWoU7t69CxMTE4waNQrbtm3D+fPnpWl27doVKSkp2LlzJwDA29sb9erVw+zZswEA2dnZcHFxwdChQzF69GhF85GWlgYrKyukpqZCo9EU5SKij1i50dv03YR/rPgpfvpuAhEVAwX5/633I02BgYHw8/ODr6+vrHtUVBRevHgh6165cmWULVsWkZGRAIDIyEhUr15dCkwAoNVqkZaWhgsXLkg1r49bq9VK48jIyEBUVJSsxsDAAL6+vlJNbtLT05GWliZ7ERER0cfLSJ8TX7NmDU6fPo2TJ0/m6JeYmAgTExNYW1vLujs6OiIxMVGqeTUw6frr+uVXk5aWhmfPnuHhw4fIysrKteby5ct5tn3y5MmYMGGCshklIiKiD57ejjTduHED33zzDVauXAlTU1N9NaPQgoODkZqaKr1u3Lih7yYRERHRO6S30BQVFYXk5GTUqVMHRkZGMDIywoEDBzBr1iwYGRnB0dERGRkZSElJkQ2XlJQEJycnAICTk1OOu+l0799Uo9FoYGZmBjs7OxgaGuZaoxtHbtRqNTQajexFREREHy+9haYWLVrg3LlziI6Oll5169ZF9+7dpb+NjY2xZ88eaZjY2FgkJCTAx8cHAODj44Nz587J7nLbvXs3NBoNqlSpItW8Og5djW4cJiYm8PLyktVkZ2djz549Ug0RERGR3q5psrS0RLVq1WTdzM3NYWtrK3Xv27cvgoKCYGNjA41Gg6FDh8LHxwcNGjQAALRq1QpVqlRBz549MXXqVCQmJmLs2LEIDAyEWq0GAAwaNAizZ8/GyJEj0adPH+zduxcRERHYtu3/7loKCgpCQEAA6tati/r16yM0NBRPnjxB796939PSICIiouJOrxeCv8mMGTNgYGCAjh07Ij09HVqtFnPnzpX6GxoaYuvWrRg8eDB8fHxgbm6OgIAATJw4UaopX748tm3bhuHDh2PmzJkoU6YMFi1aBK1WK9V06dIFd+/exbhx45CYmIhatWph586dOS4OJyIion8uvT+n6WPB5zRRYfA5TfrD5zQREfCBPaeJiIiI6EPA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1EREREChQ6NKWkpGDRokUIDg7GgwcPAACnT5/GrVu3iqxxRERERMWFUWEGOnv2LHx9fWFlZYX4+Hj0798fNjY2+OOPP5CQkIDly5cXdTuJiIiI9KpQR5qCgoLQq1cvXL16FaamplL3tm3b4uDBg0XWOCIiIqLiolCh6eTJkxg4cGCO7qVLl0ZiYuJbN4qIiIiouClUaFKr1UhLS8vR/cqVK7C3t3/rRhEREREVN4UKTZ9//jkmTpyI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REQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKaDX0DR58mTUq1cPlpaWcHBwgL+/P2JjY2U1z58/R2BgIGxtbWFhYYGOHTsiKSlJVpOQkAA/Pz+UKFECDg4OGDFiBDIzM2U1+/fvR506daBWq+Hu7o7w8PAc7ZkzZw7KlSsHU1NTeHt748SJE0U+z0RERPRh0mtoOnDgAAIDA3Hs2DHs3r0bL168QKtWrfDkyROpZvjw4fjzzz+xbt06HDhwALdv30aHDh2k/llZWfDz80NGRgaOHj2KZcuWITw8HOPGjZNq4uLi4Ofnh+bNmyM6Ohrffvst+vXrh127dkk1a9euRVBQEEJCQnD69GnUrFkTWq0WycnJ72dhEBERUbGmEkIIfTdC5+7du3BwcMCBAwfwySefIDU1Ffb29li1ahU6deoEALh8+TI8PT0RGRmJBg0aYMeOHWjXrh1u374NR0dHAEBYWBhGjRqFu3fvwsTEBKNGjcK2bdtw/vx5aVpdu3ZFSkoKdu7cCQDw9vZGvXr1MHv2bABAdnY2XFxcMHToUIwePfqNbU9LS4OVlRVSU1Oh0WiKetHQR6rc6G36bsI/VvwUP303gYiKgYL8/y5W1zSlpqYCAGxsbAAAUVFRePHiBXx9faWaypUro2zZsoiMjAQAREZGonr16lJgAgCtVou0tDRcuHBBqnl1HLoa3TgyMjIQFRUlqzEwMICvr69U87r09HSkpaXJXkRERPTxKjahKTs7G99++y0aNWqEatWqAQASExNhYmICa2trWa2joyMSExOlmlcDk66/rl9+NWlpaXj27Bnu3buHrKysXGt043jd5MmTYWVlJb1cXFwKN+NERET0QSg2oSkwMBDnz5/HmjVr9N0URYKDg5Gamiq9bty4oe8mERER0TtkpO8GAMCQIUOwdetWHDx4EGXKlJG6Ozk5ISMjAykpKbKjTUlJSXBycpJqXr/LTXd33as1r99xl5SUBI1GAzMzMxgaGsLQ0DDXGt04XqdWq6FWqws3w0RERPTB0euRJiEEhgwZgo0bN2Lv3r0oX768rL+XlxeMjY2xZ88eqVtsbCwSEhLg4+MDAPDx8cG5c+dkd7nt3r0bGo0GVapUkWpeHYeuRjcOExMTeHl5yWqys7OxZ88eqYaIiIj+2fR6pCkwMBCrVq3C5s2bYWlpKV0/ZGVlBTMzM1hZWaFv374ICgqCjY0NNBoNhg4dCh8fHzRo0AAA0KpVK1SpUgU9e/bE1KlTkZiYiLFjxyIwMFA6EjRo0CDMnj0bI0eORJ8+fbB3715ERERg27b/u3MpKCgIAQEBqFu3LurXr4/Q0FA8efIEvXv3fv8LhoiIiIodvYamefPmAQCaNWsm67506VL06tULADBjxgwYGBigY8eOSE9Ph1arxdy5c6VaQ0NDbN26FYMHD4aPjw/Mzc0REBCAiRMnSjXly5fHtm3bMHz4cMycORNlypTBokWLoNVqpZouXbrg7t27GDduHBITE1GrVi3s3Lkzx8XhRERE9M9UrJ7T9CHjc5qoMPicJv3hc5qICPiAn9NEREREVFwxNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECRvpuAClTbvQ2fTfhHyt+ip++m0BERMUAQxMR0TvALzr6wy869K7w9BwRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECvHuOiIioAHhnpP7o+85IHmkiIiIiUoChiYiIiEgBhiYiIiIiBRiaiIiIiBRgaCIiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEgBvYamgwcP4rPPPkOpUqWgUqmwadMmWX8hBMaNGwdnZ2eYmZnB19cXV69eldU8ePAA3bt3h0ajgbW1Nfr27YvHjx/Las6ePYsmTZrA1NQULi4umDp1ao62rFu3DpUrV4apqSmqV6+O7du3F/n8EhER0YdLr6HpyZMnqFmzJubMmZNr/6lTp2LWrFkICwvD8ePHYW5uDq1Wi+fPn0s13bt3x4ULF7B7925s3boVBw8exIABA6T+aWlpaNWqFVxdXREVFYVp06Zh/PjxWLBggVRz9OhRdOvWDX379sWZM2fg7+8Pf39/nD9//t3NPBEREX1QjPQ58TZt2qBNmza59hNCIDQ0FGPHjsUXX3wBAFi+fDkcHR2xadMmdO3aFZcuXcLOnTtx8uRJ1K1bFwDw22+/oW3btvjll19QqlQprFy5EhkZGViyZAlMTExQtWpVREdH49dff5XC1cyZM9G6dWuMGDECAPDDDz9g9+7dmD17NsLCwt7DkiAiIqLirthe0xQXF4fExET4+vpK3aysrODt7Y3IyEgAQGRkJKytraXABAC+vr4wMDDA8ePHpZpPPvkEJiYmUo1Wq0VsbCwePnwo1bw6HV2Nbjq5SU9PR1pamuxFREREH69iG5oSExMBAI6OjrLujo6OUr/ExEQ4ODjI+hsZGcHGxkZWk9s4Xp1GXjW6/rmZPHkyrKyspJeLi0tBZ5GIiIg+IMU2NBV3wcHBSE1NlV43btzQd5OIiIjoHSq2ocnJyQkAkJSUJOuelJQk9XNyckJycrKsf2ZmJh48eCCryW0cr04jrxpd/9yo1WpoNBrZi4iIiD5exTY0lS9fHk5OTtizZ4/ULS0tDcePH4ePjw8AwMfHBykpKYiKipJq9u7di+zsbHh7e0s1Bw8exIsXL6Sa3bt3w8PDAyVLlpRqXp2OrkY3HSIiIiK9hqbHjx8jOjoa0dHRAF5e/B0dHY2EhASoVCp8++23+PHHH7FlyxacO3cOX3/9NUqVKgV/f38AgKenJ1q3bo3+/fvjxIkTOHLkCIYMGYKuXbuiVKlSAICvvvoKJiYm6Nu3Ly5cuIC1a9di5syZCAoKktrxzTffYOfOnZg+fTouX76M8ePH49SpUxgyZMj7XiRERERUTOn1kQOnTp1C8+bNpfe6IBMQEIDw8HCMHDkST548wYABA5CSkoLGjRtj586dMDU1lYZZuXIlhgwZghYtWsDAwAAdO3bErFmzpP5WVlb466+/EBgYCC8vL9jZ2WHcuHGyZzk1bNgQq1atwtixY/Gf//wHFStWxKZNm1CtWrX3sBSIiIjoQ6DX0NSsWTMIIfLsr1KpMHHiREycODHPGhsbG6xatSrf6dSoUQOHDh3Kt6Zz587o3Llz/g0mIiKif6xie00TERERUXHC0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0ERERESkAEMTERERkQIMTUREREQKMDQRERERKcDQRERERKQAQxMRERGRAgxNRERERAowNBEREREpwNBEREREpABDExEREZECDE1ERERECjA0ERERESnA0PSaOXPmoFy5cjA1NYW3tzdOnDih7yYRERFRMcDQ9Iq1a9ciKCgIISEhOH36NGrWrAmtVovk5GR9N42IiIj0jKHpFb/++iv69++P3r17o0qVKggLC0OJEiWwZMkSfTeNiIiI9Iyh6f/LyMhAVFQUfH19pW4GBgbw9fVFZGSkHltGRERExYGRvhtQXNy7dw9ZWVlwdHSUdXd0dMTly5dz1KenpyM9PV16n5qaCgBIS0t7J+3LTn/6TsZLb/au1inA9apP73K9Aly3+sR1+/F6F+tWN04hxBtrGZoKafLkyZgwYUKO7i4uLnpoDb1LVqH6bgG9C1yvHy+u24/Xu1y3jx49gpWVVb41DE3/n52dHQwNDZGUlCTrnpSUBCcnpxz1wcHBCAoKkt5nZ2fjwYMHsLW1hUqleuft/VCkpaXBxcUFN27cgEaj0XdzqAhx3X6cuF4/Xly3uRNC4NGjRyhVqtQbaxma/j8TExN4eXlhz5498Pf3B/AyCO3ZswdDhgzJUa9Wq6FWq2XdrK2t30NLP0wajYY76UeK6/bjxPX68eK6zelNR5h0GJpeERQUhICAANStWxf169dHaGgonjx5gt69e+u7aURERKRnDE2v6NKlC+7evYtx48YhMTERtWrVws6dO3NcHE5ERET/PAxNrxkyZEiup+OocNRqNUJCQnKcyqQPH9ftx4nr9ePFdfv2VELJPXZERERE/3B8uCURERGRAgxNRERERAowNBEREREpwNBEhTJ+/HjUqlWrUMP27NkTP/30U9E2qIC6du2K6dOn67UNb6Mwy79cuXIIDQ0t8rbs2bMHnp6eyMrKKvJxvwthYWH47LPP9N2M965Zs2b49ttvFdfHx8dDpVIhOjq6yNvy/fffY8CAAUU+3nelQYMG2LBhw3ufbkHXWVFavHgxWrVqpZdp6+zcuRO1atVCdna2XtvxKoamD5wQAr6+vtBqtTn6zZ07F9bW1rh58+ZbTUOlUmHTpk1vNQ6dmJgYbN++HcOGDSv08N26dYOLiwvMzMzg6emJmTNnymr2798PlUqV45WYmCjVjB07FpMmTZJ+M1DfIiMjYWhoCD8/v/c2zaJaryNHjsTYsWNhaGgIADh8+DAaNWoEW1tbmJmZoXLlypgxY4ZsmPHjx+dYP5UrV1Y0vW3btsHb2xtmZmYoWbKk9DDa192/fx9lypSBSqVCSkqK1L1Pnz6IiopC3bp13+l+865NnjwZhoaGmDZt2nuZnm6/enVZFkZiYiJmzpyJMWPGSN0mT56MevXqwdLSEg4ODvD390dsbKxsuGbNmuXYZgYNGpTvtGJjY9G8eXM4OjrC1NQUFSpUwNixY/HixYtc69esWQOVSpVjmxo7dixGjx4t/fO+e/cuBg8ejLJly0KtVsPJyQlarRZHjhwpxBLJ2x9//IEffvihSMepxPPnz/H9998jJCRE1j0lJQWBgYFwdnaGWq1GpUqVsH379lzHMWXKFKhUqrcKfa1bt4axsTFWrlxZ6HEUNYamD5xKpcLSpUtx/PhxzJ8/X+oeFxeHkSNH4rfffkOZMmX02EK53377DZ07d4aFhYXiYe7cuYPMzEwAQFRUFBwcHLBixQpcuHABY8aMQXBwMGbPnp1juNjYWNy5c0d6OTg4SP2qVasGNzc3rFix4u1nqggsXrwYQ4cOxcGDB3H79m19N0exw4cP4/r16+jYsaPUzdzcHEOGDMHBgwdx6dIljB07FmPHjsWCBQtkw1atWlW2fg4fPvzG6W3YsAE9e/ZE7969ERMTgyNHjuCrr77KtbZv376oUaNGju4mJibo3r07HB0dP5j9JjdLlizByJEjsWTJEn03pUAWLVqEhg0bwtXVVep24MABBAYG4tixY9i9ezdevHiBVq1a4cmTJ7Jh+/fvL9tmpk6dmu+0jI2N8fXXX+Ovv/5CbGwsQkNDsXDhwhxhAHh5ZO27775DkyZNcvRr06YNHj16hB07dgAAOnbsiDNnzmDZsmW4cuUKtmzZgmbNmuH+/fuFWSR5srGxgaWlZaGHz8rKKtRRmvXr10Oj0aBRo0ZSt4yMDLRs2RLx8fFYv349YmNjsXDhQpQuXTrH8CdPnsT8+fNz3f9ep1KpEB8fn2f/Xr16YdasWQWeh3dG0EchPDxcWFhYiL///ltkZ2eL5s2bi/bt24v9+/eLevXqCRMTE+Hk5CRGjRolXrx4IQ3n6uoqZsyYIRtXzZo1RUhIiNQfgPRydXUVQggREhIiatasKZYvXy5cXV2FRqMRXbp0EWlpaXm2MTMzU1hZWYmtW7e+cX6ePXsm1qxZI1q3bi0MDQ1FSkpKnrX/+te/RPPmzaX3+/btEwDEw4cP853GhAkTROPGjd/Ylnft0aNHwsLCQly+fFl06dJFTJo0KUfN5MmThYODg7CwsBB9+vQRo0aNEjVr1pT6N23aVHzzzTeyYb744gsREBAgvX91Xee1XqOjo0WzZs2EhYWFsLS0FHXq1BEnT57Ms+2BgYGiU6dOb5zH9u3bix49ekjvddtPQbx48UKULl1aLFq06I21c+fOFU2bNhV79uzJdVs4cOCAMDExEQsWLHgn+40QQgAQCxcuFP7+/sLMzEy4u7uLzZs3y4bZvHmzcHd3F2q1WjRr1kyEh4cr2nb3798vSpcuLTIyMkSpUqXEkSNHZP0fP34sevbsKczNzYWTk5P45ZdfcmwjAMTGjRtlw1lZWYmlS5cKIYSIi4sTAMSZM2ekv1996batdevWiWrVqglTU1NhY2MjWrRoIR4/fpxn26tWrSpmz56d7/wlJycLAOLAgQNSt9y28cIYPnx4jv0+MzNTNGzYUCxatEgEBASIL774IsdwvXv3Fj169BAPHz4UAMT+/fvznc7Dhw9F3759hZ2dnbC0tBTNmzcX0dHRUn8ln6Gvz/ODBw9Ez549hbW1tTAzMxOtW7cWV65ckfovXbpUWFlZic2bNwtPT09haGgo4uLixL59+0S9evVEiRIlhJWVlWjYsKGIj4/Ps+1+fn7iu+++k3WbN2+eqFChgsjIyMh3vh89eiQqVqwodu/erWidARBxcXF59v/f//4nAIhr167lO573hUeaPhIBAQFo0aIF+vTpg9mzZ+P8+fOYMWMG2rZti3r16iEmJgbz5s3D4sWL8eOPPyoe78mTJwEAS5cuxZ07d6T3AHD9+nVs2rQJW7duxdatW3HgwAFMmTIlz3GdPXsWqampqFu3bp41kZGRGDRoEJydnREUFIRq1aohOjo6398FSk1NhY2NTY7utWrVgrOzM1q2bJnrYfP69evjxIkTSE9Pz3Pc70NERAQqV64MDw8P9OjRA0uWLIF45fFpERERGD9+PH766SecOnUKzs7OmDt37ltNM6/12r17d5QpUwYnT55EVFQURo8eDWNj4zzHc+jQoXzXJwCcOXMGR48eRdOmTWXdr169ilKlSqFChQro3r07EhIS8h3P6dOncevWLRgYGKB27dpwdnZGmzZtcP78eVndxYsXMXHiRCxfvhwGBrl/xNWtWxeZmZmoWLHiO9lvdCZMmIAvv/wSZ8+eRdu2bdG9e3c8ePAAwMujWp06dYK/vz9iYmIwcOBA2Smr/CxevBjdunWDsbExunXrhsWLF8v6jxgxAgcOHMDmzZvx119/Yf/+/Th9+nSB26/j4uIiXdOjO4I7c+ZM3LlzB926dUOfPn1w6dIl7N+/Hx06dJBtv6968OABLl68+MZtRnfa/PX9euXKlbCzs0O1atUQHByMp0+fFmg+rl27hp07d+bYFidOnAgHBwf07ds3z2Hr16+PQ4cOwcLCAhYWFti0aVO+nx2dO3dGcnIyduzYgaioKNSpUwctWrSQ1j9Q8M/QXr164dSpU9iyZQsiIyMhhEDbtm1lpxufPn2Kn3/+GYsWLcKFCxdgY2MDf39/NG3aFGfPnkVkZCQGDBiQ7w/LHz58OMc62rJlC3x8fBAYGAhHR0dUq1YNP/30U45rGQMDA+Hn5wdfX988x18QZcuWhaOjIw4dOlQk43treg5tVISSkpKEnZ2dMDAwEBs3bhT/+c9/hIeHh8jOzpZq5syZIywsLERWVpYQQvk35te/kYaEhIgSJUrIvhWNGDFCeHt759m+jRs3CkNDQ1l7hBDixo0b4scffxQVK1YUJUqUEN27dxe7du2S2pifI0eOCCMjI7Fr1y6p2+XLl0VYWJg4deqUOHLkiOjdu7cwMjISUVFRsmFjYmIEgHy/cb0PDRs2FKGhoUKIl0dT7OzsxL59+6T+Pj4+4l//+pdsGG9v77c60iRE7uvV0tJShIeHK267lZWVWL58ea79SpcuLUxMTISBgYGYOHGirN/27dtFRESEiImJETt37hQ+Pj6ibNmy+R6pXL16tQAgypYtK9avXy9OnTolunXrJmxtbcX9+/eFEEI8f/5c1KhRQ/z+++9CiPyPOpYsWVKEh4e/0/1m7Nix0vvHjx8LAGLHjh1CCCFGjRolqlWrJhvHmDFj3nikKTU1VZiZmUlHLc6cOSMsLCzEo0ePhBAvv+mbmJiIiIgIaZj79+8LMzOzQh9pEiL3ZRkVFVWgfejMmTMCgEhISMizJisrS/j5+YlGjRrJus+fP1/s3LlTnD17VqxYsUKULl1atG/fXtF0fXx8hFqtFgDEgAEDZJ8thw4dEqVLlxZ3794VQog8jzRt3rxZGBgYiKysLLF+/XpRsmRJYWpqKho2bCiCg4NFTEyMbJwajUY8f/5cNg43Nzcxf/58IYSyz9BX9+srV64IALKjivfu3RNmZmbSul66dKkAIDuidf/+fUVHxnR0R9IOHjwo6+7h4SHUarXo06ePOHXqlFizZo2wsbER48ePl2pWr14tqlWrJp49e5aj/XnBG440CSFE7dq1ZdPRJx5p+og4ODhg4MCB8PT0hL+/Py5dugQfHx/ZN4pGjRrh8ePHRXKRa7ly5WTn252dnZGcnJxn/bNnz6BWq3N8w9Fd81K9enXcuHEDK1asQKtWrfI8SqBz/vx5fPHFFwgJCZHd5eHh4YGBAwfCy8sLDRs2xJIlS9CwYcMcFyObmZkBQIG/rRal2NhYnDhxAt26dQMAGBkZoUuXLrIjB5cuXYK3t7dsOB8fn3fSnqCgIPTr1w++vr6YMmUKrl+/nm/9s2fPYGpqmmu/Q4cO4dSpUwgLC0NoaChWr14t9WvTpg06d+6MGjVqQKvVYvv27UhJSUFERAQAYNCgQdI3et31b7prM8aMGYOOHTvCy8sLS5cuhUqlwrp16wAAwcHB8PT0RI8ePd44r2ZmZnj69Ok73W9evabD3NwcGo1G2kdiY2NRr149WX39+vXfOM7Vq1fDzc0NNWvWBPDyiKqrqyvWrl0L4OXRi4yMDNk2Y2NjAw8PjwK1XYmaNWuiRYsWqF69Ojp37oyFCxfi4cOHedY/e/YMAPLcZoCXRyrOnz+PNWvWyLoPGDAAWq0W1atXR/fu3bF8+XJs3LhR2karVq0qbS9t2rSRDbt27VqcPn0aq1atwrZt2/DLL78AAB49eoSePXti4cKFsLOzy3dezczMkJ2djfT0dHTs2BG3b9/Gli1b0Lp1a+zfvx916tRBeHg4gJc3rDx+/Bi2tray7TguLk62TxXkM/TSpUswMjKSrVdbW1t4eHjg0qVLUjcTExPZdmdjY4NevXpBq9Xis88+k44Q5iWvdZSdnQ0HBwcsWLAAXl5e6NKlC8aMGYOwsDAAwI0bN/DNN99g5cqV+a7fNm3a5Ni3X113VatWzTGMbl8tDvjbcx8ZIyMjGBkpX60GBgY5DqXndWfJ614/baNSqfK96NDOzg5Pnz5FRkYGTExMpO5jx46Fs7Mzfv/9d1SqVAldu3ZFz549cwSFV128eBEtWrTAgAEDMHbs2De2tX79+jkuNNYdJre3t3/j8O/K4sWLkZmZiVKlSkndhBBQq9WYPXt2vqclX/U26/FV48ePx1dffYVt27Zhx44dCAkJwZo1a9C+fftc6+3s7PL8J1m+fHkAQPXq1ZGUlITx48dL4fB11tbWqFSpEq5duwbg5emS7777Tlbj7OwMAKhSpYrUTa1Wo0KFCtKpvb179+LcuXNYv349AEjLxM7ODmPGjMGECROkYR88eCCt+3e13xR0H1Fi8eLFuHDhgqy92dnZWLJkSb6nl16nUqneepsxNDTE7t27cfToUfz111/47bffMGbMGBw/flxa/6/SBZOHDx/mut8NGTIEW7duxcGDB994Ib7u8+HatWtwc3PD9u3bpfbrvhDpuLi4AHi57WRlZWHAgAH497//jevXryM+Pl72CArd+jEyMkJsbCzc3NwAvNxezM3NpXGbmpqiZcuWaNmyJb7//nv069cPISEh6NWrFx4/fgxnZ2fs378/R7utra2lv9/F9mFmZpbji+nSpUsxbNgw7Ny5E2vXrsXYsWOxe/duNGjQIMfwtra2UKlUOfZrZ2dnGBsbS3fJAoCnpycSExORkZGBqKgoJCcno06dOlL/rKwsHDx4ELNnz0Z6ejoMDQ2xaNEiKZgBQMWKFbF9+3bpgvLcLgd4dV/VNx5p+oh5enpK5711jhw5AktLS+kDyd7eXvatIy0tDXFxcbLxGBsbF8kzeHTPFbp48aKsu7u7OyZPnoyEhASsWrUKDx8+RPPmzVGpUiX88MMPOdpz4cIFNG/eHAEBAZg0aZKiaUdHR0v/dHXOnz+PMmXKvPEb5ruSmZmJ5cuXY/r06YiOjpZeMTExKFWqlHRkxtPTE8ePH5cNe+zYMdn719djVlZWjmt9XpfXeq1UqRKGDx+Ov/76Cx06dMDSpUvzHEft2rVzrM/c6L6h5+Xx48e4fv26tI4cHBzg7u4uvQDAy8sLarVadiv6ixcvEB8fL92JtWHDBsTExEjLctGiRQBeHvUKDAyUhrt+/TqeP3+O2rVr52hLUe03b+Lh4YFTp07Jur16zWBuzp07h1OnTmH//v2ybWb//v2IjIzE5cuX4ebmBmNjY9k28/DhQ1y5ckU2rtfn4erVq/l+m9d90Xl9m1GpVGjUqBEmTJiAM2fOwMTEBBs3bsx1HG5ubtBoNDm2GSEEhgwZgo0bN2Lv3r25Bq7X6Z4fpdtmXF1dpe0ltzu6dLKzs/HixQtkZ2ejcuXKOHfunGxZfv7552jevDmio6OlsAW8/LzIbXvRqVKlinS3X506dZCYmAgjIyPZduzu7l7ozxtPT09kZmbK1uv9+/cRGxsr+yKRl9q1ayM4OBhHjx5FtWrVsGrVqlzrTExMUKVKlRzrqFGjRrh27Zos1F25cgXOzs4wMTFBixYtcizLunXronv37oiOjpbCVunSpXPs26+uu1fvqgRePv7g+vXr+S7794lHmj5i//rXvxAaGoqhQ4diyJAhiI2NRUhICIKCgqRTX59++inCw8Px2WefwdraGuPGjZN9kwBeHkLes2cPGjVqBLVajZIlSxaqPfb29qhTpw4OHz6c64MZDQwM0KpVK7Rq1QppaWmIiIjAsmXLMH78eDx8+BAajQbnz5/Hp59+Cq1Wi6CgIOnZS4aGhtI3kdDQUJQvXx5Vq1bF8+fPsWjRIuzduxd//fWXbHqHDh3S68Pbtm7diocPH6Jv3745jih17NgRixcvxqBBg/DNN9+gV69eqFu3Lho1aoSVK1fiwoULqFChglT/6aefIigoCNu2bYObmxt+/fXXNz5P5/X1ampqihEjRqBTp04oX748bt68iZMnT8oeJ/A6rVaLZcuWybrNmTMHZcuWlZ67dPDgQfzyyy+yZ3N99913+Oyzz+Dq6orbt28jJCQEhoaGeR6JAgCNRoNBgwYhJCQELi4ucHV1lZ5R1LlzZwCQjgro3Lt3D8DLfzivfsM/dOgQKlSokKMeKLr95k0GDhyIX3/9FaNGjULfvn0RHR0tnd7J6yLdxYsXo379+vjkk09y9KtXrx4WL16MadOmoW/fvhgxYgRsbW3h4OCAMWPG5Djd/emnn2L27Nnw8fFBVlYWRo0ale9F/66urlCpVNi6dSvatm0LMzMzXLhwAXv27EGrVq3g4OCA48eP4+7du/D09Mx1HAYGBvD19cXhw4dlz0IKDAzEqlWrsHnzZlhaWkr7tZWVFczMzHD9+nWsWrUKbdu2ha2tLc6ePYvhw4fjk08+yfe29pUrV8LY2BjVq1eHWq3GqVOnEBwcjC5dusDY2BjGxsaoVq2abBjddvJ6d93nxf3799G5c2f06dMHNWrUgKWlJU6dOoWpU6fiiy++AAD4+vrCx8cH/v7+mDp1KipVqoTbt29j27ZtaN++/RsvhM9NxYoV8cUXX6B///6YP38+LC0tMXr0aJQuXVqabm7i4uKwYMECfP755yhVqhRiY2Nx9epVfP3113kOo9VqcfjwYdkzlgYPHozZs2fjm2++wdChQ3H16lX89NNP0n5taWmZY5mZm5vD1tY2R/eCOHbsGNRq9Tu7JKHA9HY1Fb0Tr9/K/aZbp1NTU0WXLl2ERqMRLi4uIjw8PMcFrVu2bBHu7u7CyMgoxyMHXjVjxgypf17mzp0rGjRoUKB5unbtmnSba0hISI5bn/HKLfNCCPHzzz8LNzc36RboZs2aib1798rG+ezZM2FlZSUiIyML1Jai1K5dO9G2bdtc+x0/flwAkC4unTRpkrCzsxMWFhYiICBAjBw5Urb8MzIyxODBg4WNjY1wcHAQkydPfuOF4K+v1/T0dNG1a1fh4uIiTExMRKlSpcSQIUOkizpzc//+fWFqaiouX74sdZs1a5aoWrWqKFGihNBoNKJ27dpi7ty5sotvu3TpIpydnYWJiYkoXbq06NKli6JbijMyMsS///1v4eDgICwtLYWvr684f/58nvV5XQjeqlUrMXnyZOn9u9hv8IYLrYXI+ciBefPmCQC5LvP09HRha2srpk6dmuu8/vzzz8LBwUFkZGSIR48eiR49eogSJUoIR0dHMXXq1BwX5d66dUu0atVKmJubi4oVK4rt27fneyG4EEJMnDhRODk5CZVKJQICAsTFixeFVqsV9vb2Qq1Wi0qVKonffvst1/bpbN++XZQuXVq2PeS2TwOQ2pKQkCA++eQTYWNjI9RqtXB3dxcjRowQqamp+U5rzZo1ok6dOsLCwkKYm5uLKlWqiJ9++infbTq3C8Fv3rwpjI2NxY0bN8Tz58/F6NGjRZ06dYSVlZUoUaKE8PDwEGPHjhVPnz6VhklLSxNDhw4VpUqVEsbGxsLFxUV0795dugheyWdoXo8csLKyEmZmZkKr1eb6yIFXJSYmCn9/f2l/c3V1FePGjcv3RpsLFy4IMzOzHI96OXr0qPD29hZqtVpUqFBBTJo0SWRmZuY5nqK4EHzAgAFi4MCB+Y7jfVIJkce9oUTvwLNnz+Dh4YG1a9fq9ZvDvHnzsHHjxhxHn6jgRowYgbS0NNlDIouzCxcu4NNPP8WVK1cUXzP2vkyaNAlhYWG4ceOGvpvyzggh4O3tjeHDh+d7ZLE4GTVqFB4+fJjjAa0fs86dO6NOnToIDg7WWxvu3bsnncZWcsr2feA1TfRemZmZYfny5dJpE30xNjbGb7/9ptc2fCzGjBkDV1fXYvX7UPm5c+cOli9fXiwC09y5c3Hy5En8/fff+P333zFt2jQEBATou1nvlEqlwoIFC6Sn/H8IHBwc9PJzJvo0bdq0Av1yw7sQHx+PuXPnFpvABAA80kREpCfDhw/H2rVr8eDBA5QtWxY9e/ZEcHBwge7kI6L3h6GJiIiISAGeniMiIiJSgKGJiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIirXIyEgYGhrCz8/vvU43IyMD06ZNQ506dWBubg4rKyvUrFkTY8eOxe3bt99rW4ioeOAjB4ioWOvXrx8sLCywePFixMbGolSpUu98munp6WjVqhXOnj2LCRMmoFGjRrC3t0dcXBxWr16NkiVLYvLkybkOm5GRIf24LRF9XHikiYiKrcePH2Pt2rUYPHgw/Pz8pB+0fdWWLVtQsWJFmJqaonnz5li2bBlUKpXsB4sPHz6MJk2awMzMDC4uLhg2bJj0i/S5mTFjBg4fPoy9e/di2LBh8PLyQtmyZdG0aVOEhYXhp59+kmqbNWuGIUOG4Ntvv4WdnR20Wi0A4MCBA6hfvz7UajWcnZ0xevRo2VOwy5Urh9DQUNl0a9WqhfHjx0vvVSoV5s2bhzZt2sDMzAwVKlTA+vXrC7YQiajIMDQRUbEVERGBypUrw8PDAz169MCSJUvw6sHxuLg4dOrUCf7+/oiJicHAgQMxZswY2TiuX7+O1q1bo2PHjjh79izWrl2Lw4cPY8iQIXlOd/Xq1WjZsiVq166da3+VSiV7v2zZMpiYmODIkSMICwvDrVu30LZtW9SrVw8xMTGYN28eFi9ejB9//LHAy+D7779Hx44dERMTg+7du6Nr1664dOlSgcdDREVAX78UTET0Jg0bNhShoaFCCCFevHgh7OzsxL59+6T+o0aNEtWqVZMNM2bMGAFAPHz4UAghRN++fcWAAQNkNYcOHRIGBgZ5/tq9qampGDZsmKybv7+/MDc3F+bm5sLHx0fq3rRpU1G7dm1Z7X/+8x/h4eEhsrOzpW5z5swRFhYW0q/Lu7q6ihkzZsiGq1mzpggJCZHeAxCDBg2S1Xh7e4vBgwfn2m4ierd4pImIiqXY2FicOHEC3bp1AwAYGRmhS5cuWLx4saymXr16suHq168vex8TE4Pw8HBYWFhIL61Wi+zsbMTFxSluz9y5cxEdHY0+ffrg6dOnsn5eXl6y95cuXYKPj4/siFSjRo3w+PFj3Lx5U/E0AcDHxyfHex5pItIP/iokERVLixcvRmZmpuzCbyEE1Go1Zs+eDSsrK0Xjefz4MQYOHIhhw4bl6Fe2bNlch6lYsSJiY2Nl3ZydnQEANjY2OerNzc0VteVVBgYGslONAPDixYsCj4eI3h8eaSKiYiczMxPLly/H9OnTER0dLb1iYmJQqlQprF69GgDg4eGBU6dOyYY9efKk7H2dOnVw8eJFuLu753jldZdbt27dsHv3bpw5c6ZQ7ff09ERkZKQsFB05cgSWlpYoU6YMAMDe3h537tyR+qelpeV65OvYsWM53nt6ehaqXUT0lvR8epCIKIeNGzcKExMTkZKSkqPfyJEjRd26dYUQQvz999/C2NhYjBw5UsTGxoq1a9eKMmXKCADSsDExMcLMzEwEBgaKM2fOiCtXrohNmzaJwMDAPKf/7Nkz0ahRI1GyZEkRGhoqoqKixN9//y127twp6tevL+rUqSPVNm3aVHzzzTey4W/evClKlCghAgMDxaVLl8SmTZuEnZ2d7Hql0aNHCycnJ3Hw4EFx9uxZ4e/vLywsLHJc02RnZycWL14sYmNjxbhx44SBgYG4cOFCIZYqEb0thiYiKnbatWsn2rZtm2u/48ePCwAiJiZGCCHE5s2bhbu7u1Cr1aJZs2Zi3rx5AoDsIu8TJ06Ili1bCgsLC2Fubi5q1KghJk2alG8bnj9/LqZMmSJq1qwpzMzMhFqtFpUrVxbDhw8XCQkJUl1uoUkIIfbv3y/q1asnTExMhJOTkxg1apR48eKF1D81NVV06dJFaDQa4eLiIsLDw3O9EHzOnDmiZcuWQq1Wi3Llyom1a9cqWYRE9A7w4ZZE9FGZNGkSwsLCcOPGDX035a2pVCps3LgR/v7++m4KEYEXghPRB27u3LmoV68ebG1tceTIEUybNi3fZzARERUWQxMRfdCuXr2KH3/8EQ8ePEDZsmXx73//G8HBwfpuFhF9hHh6joiIiEgBPnKAiIiISAGGJiIiIiIFGJqIiIiIFGBoIiIiIlKAoYmIiIhIAYYmIiIiIgUYmoiIiIgUYGgiIiIiUoChiYiIiEiB/weg9C4bdderkAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Identify the most and least profitable\n",
        "group_max = df.groupby('Product_Category')['Profit'].max()\n",
        "group_min = df.groupby('Product_Category')['Profit'].min()\n",
        "print(group_max.sum())\n",
        "print(group_min.sum())\n",
        "plt.bar(df['Profit'],)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NCrjXHlELXNq",
        "outputId": "2feaa9b6-edc4-4152-cdda-e080dd1b7bcc"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22948\n",
            "37\n"
          ]
        }
      ]
    }
  ]
}