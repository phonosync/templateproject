import pandas as pd
from ydata_profiling import ProfileReport
import argparse
import os
import sys

def main():
    """Load CSV from URL and generate data profiling report"""
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Generate data profiling report from CSV URL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py https://example.com/data.csv
  python script.py https://example.com/data.csv --output /path/to/report.html
  python script.py https://example.com/data.csv -o my_report.html
  python script.py https://example.com/data.csv --delimiter ";"
  python script.py https://example.com/data.csv -d "\\t" -o report.html
        """
    )
    
    parser.add_argument(
        'url',
        help='URL of the CSV file to profile'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='data_profile_report.html',
        help='Output path for the HTML report (default: data_profile_report.html)'
    )
    
    parser.add_argument(
        '-d', '--delimiter',
        default=',',
        help='Cell delimiter for CSV file (default: comma ",")'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate output directory exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        print(f"❌ Error: Output directory '{output_dir}' does not exist")
        sys.exit(1)
    
    print(f"📥 Loading CSV from: {args.url}")
    print(f"🔧 Using delimiter: '{args.delimiter}'")
    try:
        # Load CSV directly into DataFrame with specified delimiter
        df = pd.read_csv(args.url, sep=args.delimiter)
        print(f"✅ CSV loaded successfully: {len(df)} rows × {len(df.columns)} columns")
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        sys.exit(1)
    
    print("📊 Generating data profiling report...")
    try:
        # Create profiling report
        profile = ProfileReport(df, title="Data Profiling Report")
        
        # Save to HTML
        profile.to_file(args.output)
        print(f"✅ Data profiling report saved as '{args.output}'")
        print(f"📖 Open the HTML file in your browser to view the report")
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()