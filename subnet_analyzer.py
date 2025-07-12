import pandas as pd
import ipaddress

def calculate_subnet(ip, subnet_mask):
    """Calculate subnet information for a given IP and mask"""
    net = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
    return {
        "CIDR": str(net.with_prefixlen),
        "Network Address": str(net.network_address),
        "Broadcast Address": str(net.broadcast_address),
        "Usable Hosts": net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses
    }

def analyze_subnets(input_file="ip_data.xlsx", output_file="subnet_report.csv"):
    """Main function to analyze subnets from Excel and save results"""
    try:
        df = pd.read_excel(input_file)
        
        if not {'IP Address', 'Subnet Mask'}.issubset(df.columns):
            raise ValueError("Excel file must contain 'IP Address' and 'Subnet Mask' columns")
        
        results = []
        error_count = 0
        
        for _, row in df.iterrows():
            ip = str(row['IP Address']).strip()
            subnet_mask = str(row['Subnet Mask']).strip()
            
            try:
                results.append({
                    "IP Address": ip,
                    "Subnet Mask": subnet_mask,
                    **calculate_subnet(ip, subnet_mask)
                })
            except ValueError as e:
                error_count += 1
                print(f"Error processing {ip}/{subnet_mask}: {e}")
                results.append({
                    "IP Address": ip,
                    "Subnet Mask": subnet_mask,
                    "Error": str(e)
                })
        
        pd.DataFrame(results).to_csv(output_file, index=False)
        print(f"Report generated: {output_file}")
        print(f"Errors encountered: {error_count}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    analyze_subnets()