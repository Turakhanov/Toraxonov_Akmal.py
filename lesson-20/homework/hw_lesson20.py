{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4881344c",
   "metadata": {},
   "source": [
    "Customer Purchases Analysis:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "074ce5b4",
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
       "      <th>CustomerId</th>\n",
       "      <th>FirstName</th>\n",
       "      <th>LastName</th>\n",
       "      <th>UnitPrice</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>Helena</td>\n",
       "      <td>Holý</td>\n",
       "      <td>49.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>26</td>\n",
       "      <td>Richard</td>\n",
       "      <td>Cunningham</td>\n",
       "      <td>47.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>56</th>\n",
       "      <td>57</td>\n",
       "      <td>Luis</td>\n",
       "      <td>Rojas</td>\n",
       "      <td>46.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>45</td>\n",
       "      <td>Ladislav</td>\n",
       "      <td>Kovács</td>\n",
       "      <td>45.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>46</td>\n",
       "      <td>Hugh</td>\n",
       "      <td>O'Reilly</td>\n",
       "      <td>45.62</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    CustomerId FirstName    LastName  UnitPrice\n",
       "5            6    Helena        Holý      49.62\n",
       "25          26   Richard  Cunningham      47.62\n",
       "56          57      Luis       Rojas      46.62\n",
       "44          45  Ladislav      Kovács      45.62\n",
       "45          46      Hugh    O'Reilly      45.62"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "conn = sqlite3.connect(r\"C:\\Users\\Asus\\Downloads\\chinook.db\")\n",
    "\n",
    "\n",
    "customers = pd.read_sql(\"SELECT * FROM customers\", conn)\n",
    "invoices = pd.read_sql(\"SELECT * FROM Invoices\", conn)\n",
    "invoice_items = pd.read_sql(\"SELECT * FROM Invoice_items\", conn)\n",
    "tracks = pd.read_sql(\"SELECT TrackId, AlbumId FROM tracks\", conn)\n",
    "albums = pd.read_sql(\"SELECT * FROM playlists\", conn)\n",
    "\n",
    "invoice_details = pd.merge(invoice_items,invoices, on='InvoiceId')\n",
    "total_per_customer = invoice_details.groupby('CustomerId')['UnitPrice'].sum().reset_index()\n",
    "total_per_customer = pd.merge(total_per_customer,customers[['CustomerId','FirstName','LastName']],on='CustomerId')\n",
    "\n",
    "top5 = total_per_customer.sort_values(('UnitPrice'), ascending = False).head(5)\n",
    "top5 = top5[['CustomerId','FirstName','LastName','UnitPrice']]\n",
    "top5\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9708c107",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PurchaseType\n",
       "Individual    100.0\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "invoice_data = pd.merge(invoice_items, invoices, on='InvoiceId')\n",
    "\n",
    "# Step 2: Merge with tracks (to get AlbumId)\n",
    "invoice_tracks = pd.merge(invoice_data, tracks, on='TrackId')\n",
    "customer_album_counts = invoice_tracks.groupby(['CustomerId','AlbumId']).size().reset_index(name='TracksBought')\n",
    "album_track_counts = tracks.groupby('AlbumId').size().reset_index(name='TotalTracks')\n",
    "merged = pd.merge(customer_album_counts,album_track_counts,on='AlbumId')\n",
    "merged['PurchaseType'] = merged.apply(\n",
    "    lambda x: 'Album' if x['TracksBought'] == x['TotalTracks'] else 'Individual', axis =1\n",
    ")\n",
    "\n",
    "customer_pref = merged.groupby('CustomerId')['PurchaseType'].apply(\n",
    "    lambda x: x.mode()[0]\n",
    ").reset_index()\n",
    "\n",
    "summary = customer_pref['PurchaseType'].value_counts(normalize=True)*100\n",
    "summary\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfb654c0",
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
