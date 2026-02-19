import sys
import os
import argparse

# Add the project root to sys.path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.simulation import Simulation
from universe.base_world import WorldRegistry

def main():
    parser = argparse.ArgumentParser(description="RIW2 CLI - World Engine")
    parser.add_argument("--tick-rate", type=float, default=1.0, help="Seconds per tick (default: 1.0)")
    parser.add_argument("--world", type=str, default="default_world", help="World ID to simulate")
    parser.add_argument("--no-story", action="store_true", help="Disable story generation")
    parser.add_argument("--save-interval", type=int, default=30, help="Ticks between auto-saves")
    
    args = parser.parse_args()

    print(f"RIW2 CLI - Starting Simulation: {args.world}")
    
    # In a real scenario, we might load the world from the registry or a factory
    # For now, we'll pass the world_id to the simulation or let it handle it
    
    sim = Simulation(
        tick_rate=args.tick_rate,
        auto_save_interval=args.save_interval,
        enable_story_generation=not args.no_story
    )
    
    try:
        sim.start()
    except KeyboardInterrupt:
        sim.stop()
        print("\nSimulation terminated.")

if __name__ == "__main__":
    main()
