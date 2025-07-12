import pandas as pd
import matplotlib.pyplot as plt

def create_visualization(input_file="subnet_report.csv", output_file="network_plot.png"):
    """Create visualization of subnet host distribution with enhanced features"""
    try:
        df = pd.read_csv(input_file)
        valid_subnets = df[~df['CIDR'].isna()]
        
        if valid_subnets.empty:
            print("No valid subnets to visualize")
            return
            
        grouped = valid_subnets.groupby('CIDR')['Usable Hosts'].sum().sort_values()
        
        plt.figure(figsize=(12, 6))
        
        colors = ['#1f77b4' if x < 500 else '#ff7f0e' for x in grouped.values]
        
        bars = plt.bar(grouped.index, grouped.values, color=colors)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', 
                    ha='center', 
                    va='bottom',
                    fontsize=9)
        
        # Formatting
        plt.xlabel("Subnet (CIDR Notation)", fontsize=10)
        plt.ylabel("Number of Usable Hosts", fontsize=10)
        plt.title("Usable Hosts per Subnet", fontsize=12)
        plt.xticks(rotation=45, fontsize=8)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Save and show result
        plt.tight_layout()
        plt.savefig(output_file, dpi=100)
        print(f"Visualization saved: {output_file}")
        
    except Exception as e:
        print(f"Error creating visualization: {str(e)}")

if __name__ == "__main__":
    create_visualization()