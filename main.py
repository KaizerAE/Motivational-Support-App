import time

def main():
    """Continuously print 'Everything will be OK.' to provide motivation and encouragement."""
    print("\n" + "="*50)
    print("  🌟 EVERYTHING WILL BE OK 🌟")
    print("="*50 + "\n")
    
    while True:
        print("✨ Everything will be OK. ✨")
        time.sleep(3)  # Wait 3 seconds between messages

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "="*50)
        print("  💚 Thank you for the positive vibes! 💚")
        print("  Remember: Everything will be OK!")
        print("="*50 + "\n")
