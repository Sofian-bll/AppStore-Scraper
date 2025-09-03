import pandas as pd
import requests
import time
from typing import Dict, Optional

class CurrencyConverter:
    def __init__(self):
        # API gratuite pour les taux de change
        self.base_url = "https://api.exchangerate-api.com/v4/latest"
        self.rates_cache = {}
        
    def get_exchange_rate(self, from_currency: str, to_currency: str = "EUR") -> Optional[float]:
        """
        Récupère le taux de change d'une devise vers l'EUR
        """
        if from_currency == to_currency:
            return 1.0
            
        # Vérifier le cache
        cache_key = f"{from_currency}_to_{to_currency}"
        if cache_key in self.rates_cache:
            return self.rates_cache[cache_key]
        
        try:
            # Faire l'appel API
            url = f"{self.base_url}/{from_currency}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if to_currency in data['rates']:
                rate = data['rates'][to_currency]
                self.rates_cache[cache_key] = rate
                return rate
            else:
                print(f"Devise {to_currency} non trouvée pour {from_currency}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération du taux pour {from_currency}: {e}")
            return None
        except KeyError as e:
            print(f"Erreur dans la structure de la réponse pour {from_currency}: {e}")
            return None
    
    def convert_price(self, price: float, from_currency: str, to_currency: str = "EUR") -> Optional[float]:
        """
        Convertit un prix d'une devise vers une autre
        """
        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate is not None:
            return round(price * rate, 2)
        return None

def process_csv_file(input_file: str, output_file: str):
    """
    Traite le fichier CSV et ajoute les prix convertis en euros
    """
    print(f"Lecture du fichier {input_file}...")
    
    try:
        # Lire le CSV
        df = pd.read_csv(input_file)
        
        print(f"Fichier lu avec succès. {len(df)} lignes trouvées.")
        print("Colonnes disponibles:", list(df.columns))
        
        # Vérifier que les colonnes nécessaires existent
        required_columns = ['price', 'currency']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Colonnes manquantes: {missing_columns}")
        
        # Initialiser le convertisseur
        converter = CurrencyConverter()
        
        # Ajouter une colonne pour les prix en euros
        df['price_eur'] = None
        
        # Obtenir la liste unique des devises
        unique_currencies = df['currency'].unique()
        print(f"Devises trouvées: {list(unique_currencies)}")
        
        # Convertir les prix
        print("Conversion des prix en cours...")
        
        for index, row in df.iterrows():
            price = row['price']
            currency = row['currency']
            
            if pd.isna(price) or pd.isna(currency):
                print(f"Ligne {index}: prix ou devise manquant")
                continue
            
            # Convertir le prix
            converted_price = converter.convert_price(price, currency, "EUR")
            df.at[index, 'price_eur'] = converted_price
            
            # Afficher le progrès
            if (index + 1) % 20 == 0:
                print(f"Progression: {index + 1}/{len(df)} lignes traitées")
            
            # Petite pause pour éviter de surcharger l'API
            time.sleep(0.1)
        
        print("Conversion terminée!")
        
        # Sauvegarder le résultat
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Fichier sauvegardé: {output_file}")
        
        # Afficher un résumé
        print("\n=== RÉSUMÉ ===")
        print(f"Total des lignes: {len(df)}")
        print(f"Conversions réussies: {df['price_eur'].notna().sum()}")
        print(f"Conversions échouées: {df['price_eur'].isna().sum()}")
        
        # Afficher quelques exemples
        print("\n=== EXEMPLES DE CONVERSION ===")
        sample_df = df[df['price_eur'].notna()].head(10)
        for _, row in sample_df.iterrows():
            print(f"{row['name']}: {row['price']} {row['currency']} → {row['price_eur']} EUR")
        
        return df
        
    except FileNotFoundError:
        print(f"Erreur: Le fichier {input_file} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Erreur lors du traitement: {e}")
        return None

def main():
    """
    Fonction principale
    """
    input_file = "Claude Price/in_app_purchases.csv"
    output_file = "Claude Price/in_app_purchases_with_eur.csv"
    
    print("=== CONVERTISSEUR DE PRIX EN EUROS ===\n")
    
    # Traiter le fichier
    result_df = process_csv_file(input_file, output_file)
    
    if result_df is not None:
        print(f"\n✅ Traitement terminé avec succès!")
        print(f"Le fichier de sortie '{output_file}' contient maintenant une colonne 'price_eur' avec les prix convertis.")
    else:
        print("\n❌ Échec du traitement.")

if __name__ == "__main__":
    # Installation des dépendances requises
    print("Assurez-vous d'avoir installé les dépendances:")
    print("pip install pandas requests")
    print()
    
    main()