import os

def file_read_write_challenge():
    """Part 1: File Read & Write Challenge"""
    print("\n--- File Read & Write Challenge ---")
    
    # Get file paths with defaults
    input_file = input("Enter input filename [default: input.txt]: ") or "input.txt"
    output_file = input("Enter output filename [default: output.txt]: ") or "output.txt"
    
    try:
        # Verify input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"'{input_file}' not found in {os.getcwd()}")
            
        # Read and process file
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Modify content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Write output
        with open(output_file, 'w') as f:
            f.write(modified_content)
            
        print(f"\nSuccess! Modified content written to '{output_file}'")
        print(f"Original size: {len(content)} bytes | New size: {len(modified_content)} bytes")
        
    except FileNotFoundError as e:
        print(f"\nError: {str(e)}")
    except PermissionError:
        print("\nError: Permission denied. Check file access rights.")
    except IOError as e:
        print(f"\nIO Error: {str(e)}")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")

def error_handling_lab():
    """Part 2: Error Handling Lab"""
    print("\n--- Error Handling Lab ---")
    print("Type 'quit' to exit at any time")
    
    while True:
        filename = input("\nEnter filename to read: ").strip()
        
        if filename.lower() == 'quit':
            print("Exiting error handling lab...")
            break
            
        try:
            # Verify file exists first
            if not os.path.exists(filename):
                raise FileNotFoundError(f"'{filename}' not found")
                
            # Check if it's a file (not directory)
            if not os.path.isfile(filename):
                raise IOError(f"'{filename}' is not a regular file")
                
            # Check read access
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"No read permission for '{filename}'")
                
            # Read and display file
            with open(filename, 'r') as f:
                content = f.read()
                
            print(f"\n--- Contents of '{filename}' ---")
            print(content)
            print(f"\nFile info: {os.path.getsize(filename)} bytes | Last modified: {os.path.getmtime(filename)}")
            break
                
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")
        except PermissionError as e:
            print(f"Error: {str(e)}")
        except UnicodeDecodeError:
            print("Error: Could not decode as text file (try binary file?)")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

def main_menu():
    """Main program menu"""
    print("\n" + "="*40)
    print("File Handling Assignment")
    print("="*40)
    
    while True:
        print("\nMain Menu:")
        print("1. File Read & Write Challenge")
        print("2. Error Handling Lab")
        print("3. Exit")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == '1':
            file_read_write_challenge()
        elif choice == '2':
            error_handling_lab()
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()