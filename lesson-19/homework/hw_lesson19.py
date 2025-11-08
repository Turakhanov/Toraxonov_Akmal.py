{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e97cfcd7",
   "metadata": {},
   "source": [
    "Homework 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0252cc85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"2\" halign=\"left\">Quantity</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>sum</th>\n",
       "      <th>max</th>\n",
       "      <th>mean</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Category</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Clothing</th>\n",
       "      <td>157</td>\n",
       "      <td>15</td>\n",
       "      <td>31.176471</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Electronics</th>\n",
       "      <td>183</td>\n",
       "      <td>15</td>\n",
       "      <td>276.764706</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Home</th>\n",
       "      <td>144</td>\n",
       "      <td>14</td>\n",
       "      <td>55.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Quantity           Price\n",
       "                 sum max        mean\n",
       "Category                            \n",
       "Clothing         157  15   31.176471\n",
       "Electronics      183  15  276.764706\n",
       "Home             144  14   55.000000"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "sales_df = pd.read_csv(r\"C:\\Users\\Asus\\Downloads\\sales_data.csv\")\n",
    "\n",
    "category_stats = sales_df.groupby('Category').agg({\n",
    "    'Quantity': ['sum', 'max'],\n",
    "    'Price': 'mean'\n",
    "})\n",
    "\n",
    "category_stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8cafd68a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Category     Product        \n",
       "Clothing     Jeans              15\n",
       "Electronics  Smart TV           15\n",
       "Home         Pressure Cooker    14\n",
       "Name: Quantity, dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum()\n",
    "top_products = top_products.groupby(level=0, group_keys=False).nlargest(1)\n",
    "top_products"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d8467f12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2023-01-07'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_df['Total Sales'] = sales_df['Quantity'] * sales_df['Price']\n",
    "date_max_sale = sales_df.groupby('Date')['Total Sales'].sum().idxmax()\n",
    "date_max_sale"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7bced48f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CustomerID\n",
      "101    21\n",
      "102    21\n",
      "103    20\n",
      "104    20\n",
      "Name: OrderID, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "customer_orders_df = pd.read_csv(r\"C:\\Users\\Asus\\Downloads\\customer_orders.csv\")\n",
    "\n",
    "orders_count = customer_orders_df.groupby('CustomerID')['OrderID'].count()\n",
    "customer_20plus = orders_count[orders_count>=20]\n",
    "print(customer_20plus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6320f7fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CustomerID\n",
       "102    138.095238\n",
       "104    169.750000\n",
       "Name: Price, dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_price_per_customer = customer_orders_df.groupby('CustomerID')['Price'].mean()\n",
    "expensive_customer = avg_price_per_customer[avg_price_per_customer>120]\n",
    "expensive_customer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "520efc4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Quantity</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Product</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Cargo Pants</th>\n",
       "      <td>6</td>\n",
       "      <td>180</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dress Shirt</th>\n",
       "      <td>5</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Formal Shirt</th>\n",
       "      <td>6</td>\n",
       "      <td>210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Smartphone</th>\n",
       "      <td>5</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sport Shoes</th>\n",
       "      <td>5</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sunglasses</th>\n",
       "      <td>5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wireless Earbuds</th>\n",
       "      <td>6</td>\n",
       "      <td>720</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Quantity  Price\n",
       "Product                          \n",
       "Cargo Pants              6    180\n",
       "Dress Shirt              5    125\n",
       "Formal Shirt             6    210\n",
       "Smartphone               5   2000\n",
       "Sport Shoes              5    200\n",
       "Sunglasses               5     75\n",
       "Wireless Earbuds         6    720"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_stats = customer_orders_df.groupby('Product').agg({\n",
    "    'Quantity':'sum',\n",
    "    'Price': lambda x: (x*customer_orders_df.loc[x.index, 'Quantity']).sum()\n",
    "})\n",
    "product_stats_filtered = product_stats[product_stats['Quantity']>=5]\n",
    "product_stats_filtered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "299dd99f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>id</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>salary</th>\n",
       "      <th>state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Armin</td>\n",
       "      <td>Coltart</td>\n",
       "      <td>acoltart0@abc.net.au</td>\n",
       "      <td>Male</td>\n",
       "      <td>368693</td>\n",
       "      <td>District of Columbia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Mia</td>\n",
       "      <td>Tuddenham</td>\n",
       "      <td>mtuddenham1@addthis.com</td>\n",
       "      <td>Female</td>\n",
       "      <td>154398</td>\n",
       "      <td>Florida</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Kirsteni</td>\n",
       "      <td>Brafield</td>\n",
       "      <td>kbrafield2@arizona.edu</td>\n",
       "      <td>Female</td>\n",
       "      <td>1230304</td>\n",
       "      <td>Georgia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Phylis</td>\n",
       "      <td>Furlong</td>\n",
       "      <td>pfurlong3@merriam-webster.com</td>\n",
       "      <td>Female</td>\n",
       "      <td>1567795</td>\n",
       "      <td>California</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Wandis</td>\n",
       "      <td>Loveredge</td>\n",
       "      <td>wloveredge4@hatena.ne.jp</td>\n",
       "      <td>Female</td>\n",
       "      <td>1136950</td>\n",
       "      <td>Alabama</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id first_name  last_name                          email  gender   salary  \\\n",
       "0   1      Armin    Coltart           acoltart0@abc.net.au    Male   368693   \n",
       "1   2        Mia  Tuddenham        mtuddenham1@addthis.com  Female   154398   \n",
       "2   3   Kirsteni   Brafield         kbrafield2@arizona.edu  Female  1230304   \n",
       "3   4     Phylis    Furlong  pfurlong3@merriam-webster.com  Female  1567795   \n",
       "4   5     Wandis  Loveredge       wloveredge4@hatena.ne.jp  Female  1136950   \n",
       "\n",
       "                  state  \n",
       "0  District of Columbia  \n",
       "1               Florida  \n",
       "2               Georgia  \n",
       "3            California  \n",
       "4               Alabama  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sqlite3 as sql\n",
    "\n",
    "conn = sql.connect(r\"C:\\Users\\Asus\\Downloads\\population.db\")\n",
    "population_df = pd.read_sql(\"SELECT * from population\",conn)\n",
    "conn.close()\n",
    "\n",
    "population_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3c08837d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Salary Band</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Average Salary</th>\n",
       "      <th>Median Salary</th>\n",
       "      <th>Number of population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>till $200,000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>$200,001 - $400,000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>$400,001 - $600,000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>$600,001 - $800,000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>$800,001 - $1,000,000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Salary Band  Percentage  Average Salary  Median Salary  \\\n",
       "0          till $200,000         NaN             NaN            NaN   \n",
       "1    $200,001 - $400,000         NaN             NaN            NaN   \n",
       "2    $400,001 - $600,000         NaN             NaN            NaN   \n",
       "3    $600,001 - $800,000         NaN             NaN            NaN   \n",
       "4  $800,001 - $1,000,000         NaN             NaN            NaN   \n",
       "\n",
       "   Number of population  \n",
       "0                   NaN  \n",
       "1                   NaN  \n",
       "2                   NaN  \n",
       "3                   NaN  \n",
       "4                   NaN  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "salary_band = pd.read_excel(r\"C:\\Users\\Asus\\Downloads\\population_salary_analysis.xlsx\")\n",
    "salary_band.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "95937a4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Salary SalaryBand\n",
      "0   25000        Low\n",
      "1   45000     Medium\n",
      "2   75000       High\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Example salaries\n",
    "population_df = pd.DataFrame({'Salary':[25000, 45000, 75000]})\n",
    "\n",
    "# Define bands\n",
    "bins = [0, 30000, 60000, 100000]  # lower and upper bounds\n",
    "labels = ['Low', 'Medium', 'High']\n",
    "\n",
    "# Assign SalaryBand\n",
    "population_df['SalaryBand'] = pd.cut(population_df['Salary'], bins=bins, labels=labels)\n",
    "print(population_df)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d040b816",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            PopulationCount  AvgSalary  MedianSalary  Percentage\n",
      "SalaryBand                                                      \n",
      "Low                       1    25000.0       25000.0   33.333333\n",
      "Medium                    1    45000.0       45000.0   33.333333\n",
      "High                      1    75000.0       75000.0   33.333333\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Asus\\AppData\\Local\\Temp\\ipykernel_10688\\2814511069.py:1: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  band_stats = population_df.groupby('SalaryBand').agg(\n"
     ]
    }
   ],
   "source": [
    "band_stats = population_df.groupby('SalaryBand').agg(\n",
    "    PopulationCount=('Salary', 'count'),\n",
    "    AvgSalary=('Salary', 'mean'),\n",
    "    MedianSalary=('Salary', 'median')\n",
    ")\n",
    "\n",
    "band_stats['Percentage'] = (band_stats['PopulationCount'] / population_df.shape[0]) * 100\n",
    "\n",
    "print(band_stats)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ba92aa8c",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'State'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[28]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m state_stats = \u001b[43mpopulation_df\u001b[49m\u001b[43m.\u001b[49m\u001b[43mgroupby\u001b[49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mState\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mSalaryBand\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m.agg(\n\u001b[32m      2\u001b[39m     PopulationCount=(\u001b[33m'\u001b[39m\u001b[33mSalary\u001b[39m\u001b[33m'\u001b[39m,\u001b[33m'\u001b[39m\u001b[33mcount\u001b[39m\u001b[33m'\u001b[39m),\n\u001b[32m      3\u001b[39m     AvgSalary=(\u001b[33m'\u001b[39m\u001b[33mSalary\u001b[39m\u001b[33m'\u001b[39m,\u001b[33m'\u001b[39m\u001b[33mmean\u001b[39m\u001b[33m'\u001b[39m),\n\u001b[32m      4\u001b[39m     MedianSalary=(\u001b[33m'\u001b[39m\u001b[33mSalary\u001b[39m\u001b[33m'\u001b[39m,\u001b[33m'\u001b[39m\u001b[33mmedian\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m      5\u001b[39m )\n\u001b[32m      7\u001b[39m state_stats[\u001b[33m'\u001b[39m\u001b[33mPercentage\u001b[39m\u001b[33m'\u001b[39m] = state_stats.groupby(level=\u001b[32m0\u001b[39m)[\u001b[33m'\u001b[39m\u001b[33mPopulationCount\u001b[39m\u001b[33m'\u001b[39m].apply(\u001b[38;5;28;01mlambda\u001b[39;00m x: x / x.sum() * \u001b[32m100\u001b[39m)\n\u001b[32m      8\u001b[39m \u001b[38;5;28mprint\u001b[39m(state_stats)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Asus\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\frame.py:9210\u001b[39m, in \u001b[36mDataFrame.groupby\u001b[39m\u001b[34m(self, by, axis, level, as_index, sort, group_keys, observed, dropna)\u001b[39m\n\u001b[32m   9207\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m level \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m by \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m   9208\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[33m\"\u001b[39m\u001b[33mYou have to supply one of \u001b[39m\u001b[33m'\u001b[39m\u001b[33mby\u001b[39m\u001b[33m'\u001b[39m\u001b[33m and \u001b[39m\u001b[33m'\u001b[39m\u001b[33mlevel\u001b[39m\u001b[33m'\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m-> \u001b[39m\u001b[32m9210\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mDataFrameGroupBy\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   9211\u001b[39m \u001b[43m    \u001b[49m\u001b[43mobj\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m   9212\u001b[39m \u001b[43m    \u001b[49m\u001b[43mkeys\u001b[49m\u001b[43m=\u001b[49m\u001b[43mby\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9213\u001b[39m \u001b[43m    \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m=\u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9214\u001b[39m \u001b[43m    \u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9215\u001b[39m \u001b[43m    \u001b[49m\u001b[43mas_index\u001b[49m\u001b[43m=\u001b[49m\u001b[43mas_index\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9216\u001b[39m \u001b[43m    \u001b[49m\u001b[43msort\u001b[49m\u001b[43m=\u001b[49m\u001b[43msort\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9217\u001b[39m \u001b[43m    \u001b[49m\u001b[43mgroup_keys\u001b[49m\u001b[43m=\u001b[49m\u001b[43mgroup_keys\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9218\u001b[39m \u001b[43m    \u001b[49m\u001b[43mobserved\u001b[49m\u001b[43m=\u001b[49m\u001b[43mobserved\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9219\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdropna\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdropna\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   9220\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Asus\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:1331\u001b[39m, in \u001b[36mGroupBy.__init__\u001b[39m\u001b[34m(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, observed, dropna)\u001b[39m\n\u001b[32m   1328\u001b[39m \u001b[38;5;28mself\u001b[39m.dropna = dropna\n\u001b[32m   1330\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m grouper \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1331\u001b[39m     grouper, exclusions, obj = \u001b[43mget_grouper\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   1332\u001b[39m \u001b[43m        \u001b[49m\u001b[43mobj\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1333\u001b[39m \u001b[43m        \u001b[49m\u001b[43mkeys\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1334\u001b[39m \u001b[43m        \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m=\u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1335\u001b[39m \u001b[43m        \u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1336\u001b[39m \u001b[43m        \u001b[49m\u001b[43msort\u001b[49m\u001b[43m=\u001b[49m\u001b[43msort\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1337\u001b[39m \u001b[43m        \u001b[49m\u001b[43mobserved\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mobserved\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01mis\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mlib\u001b[49m\u001b[43m.\u001b[49m\u001b[43mno_default\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01melse\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mobserved\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1338\u001b[39m \u001b[43m        \u001b[49m\u001b[43mdropna\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mdropna\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1339\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1341\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m observed \u001b[38;5;129;01mis\u001b[39;00m lib.no_default:\n\u001b[32m   1342\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28many\u001b[39m(ping._passed_categorical \u001b[38;5;28;01mfor\u001b[39;00m ping \u001b[38;5;129;01min\u001b[39;00m grouper.groupings):\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Asus\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\groupby\\grouper.py:1043\u001b[39m, in \u001b[36mget_grouper\u001b[39m\u001b[34m(obj, key, axis, level, sort, observed, validate, dropna)\u001b[39m\n\u001b[32m   1041\u001b[39m         in_axis, level, gpr = \u001b[38;5;28;01mFalse\u001b[39;00m, gpr, \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m   1042\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1043\u001b[39m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(gpr)\n\u001b[32m   1044\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(gpr, Grouper) \u001b[38;5;129;01mand\u001b[39;00m gpr.key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m   1045\u001b[39m     \u001b[38;5;66;03m# Add key to exclusions\u001b[39;00m\n\u001b[32m   1046\u001b[39m     exclusions.add(gpr.key)\n",
      "\u001b[31mKeyError\u001b[39m: 'State'"
     ]
    }
   ],
   "source": [
    "state_stats = population_df.groupby(['State','SalaryBand']).agg(\n",
    "    PopulationCount=('Salary','count'),\n",
    "    AvgSalary=('Salary','mean'),\n",
    "    MedianSalary=('Salary','median')\n",
    ")\n",
    "\n",
    "state_stats['Percentage'] = state_stats.groupby(level=0)['PopulationCount'].apply(lambda x: x / x.sum() * 100)\n",
    "print(state_stats)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab3f2881",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
