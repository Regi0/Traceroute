import subprocess
import datetime
import os

def perform_traceroute(host):
    try:
        # Run the traceroute command and capture output
        result = subprocess.run(
            ["traceroute", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Return the output
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error executing traceroute: {e}"

def main():
    # Prompt the user for the input file
    input_file = input("Enter the name of the file containing hostnames/IP addresses: ").strip()

    # Check if the file exists
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist. Please check the file name and try again.")
        return

    # Get the timestamp for the output file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{os.path.splitext(input_file)[0]}_{timestamp}.txt"

    # Read the hostnames/IPs from the input file
    try:
        with open(input_file, "r") as file:
            hosts = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file '{input_file}': {e}")
        return

    # Open the output file for writing results
    with open(output_file, "w") as file:
        for host in hosts:
            # Add a timestamp for this test
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Traceroute for: {host}\n")
            file.write(f"Timestamp: {current_time}\n")
            file.write("=" * 40 + "\n")
            # Perform traceroute
            result = perform_traceroute(host)
            file.write(result)
            file.write("\n\n")  # Add an empty line for readability

    print(f"Traceroute results written to: {output_file}")

if __name__ == "__main__":
    main()