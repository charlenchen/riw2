"""
Universe-level state management for RIWA2.
Tracks cosmic resources, stellar parameters, and escape conditions.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum
import json


class SourceEnergyLevel(Enum):
    """Energy classification in RIWA2 universe."""
    E_COMMON = "E_Common"           # Daily consumption, renewable
    D_RARE = "D_Rare"               # Cross-world travel, ability enhancement
    C_PRECIOUS = "C_Precious"        # History rewrite, world repair
    B_LEGENDARY = "B_Legendary"      # Cross-dimensional comms, life transfer
    A_SACRED = "A_Sacred"            # Terminal gateway keys (7 required for escape)
    OMEGA_ABSOLUTE = "Omega_Absolute"  # Only at universe genesis (depleted)


@dataclass
class SourceEnergyFragment:
    """A piece of source energy with grade and location."""
    id: str
    level: SourceEnergyLevel
    location_world: str  # Which world it's in
    location_coordinates: Dict[str, float]  # x, y, z in that world
    discovered_by: Optional[str] = None  # UUID of discovering entity
    collected_by: Optional[str] = None   # UUID of collector
    collection_timestamp: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'level': self.level.value,
            'location_world': self.location_world,
            'location_coordinates': self.location_coordinates,
            'discovered_by': self.discovered_by,
            'collected_by': self.collected_by,
            'collection_timestamp': self.collection_timestamp
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'SourceEnergyFragment':
        return cls(
            id=data['id'],
            level=SourceEnergyLevel(data['level']),
            location_world=data['location_world'],
            location_coordinates=data['location_coordinates'],
            discovered_by=data.get('discovered_by'),
            collected_by=data.get('collected_by'),
            collection_timestamp=data.get('collection_timestamp')
        )


@dataclass
class StarData:
    """Physical parameters of a star hosting RIWA2 Celestial Core."""
    name: str                      # e.g., "Sol-001"
    catalog_id: str                # Unique identifier
    lifespan_remaining_years: float  # How long until supernova/death
    fusion_power_output_watts: float  # Energy available (theoretical)
    protection_shield_status: float  # 0.0 to 1.0, degradation over time
    cloaking_field_active: bool    # High-dimensional invisibility
    
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'catalog_id': self.catalog_id,
            'lifespan_remaining_years': self.lifespan_remaining_years,
            'fusion_power_output_watts': self.fusion_power_output_watts,
            'protection_shield_status': self.protection_shield_status,
            'cloaking_field_active': self.cloaking_field_active
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'StarData':
        return cls(
            name=data['name'],
            catalog_id=data['catalog_id'],
            lifespan_remaining_years=data['lifespan_remaining_years'],
            fusion_power_output_watts=data['fusion_power_output_watts'],
            protection_shield_status=data['protection_shield_status'],
            cloaking_field_active=data['cloaking_field_active']
        )


@dataclass
class UniverseMigrationPlan:
    """Schedule for Celestial Core migration to next star."""
    current_star: StarData
    next_star_name: str
    next_star_distance_ly: float  # Light years
    replication_units_deployed: int  # How many copies are waiting at next star
    estimated_migration_year: int  # Cosmic year when migration will occur
    migration_in_progress: bool = False
    
    def to_dict(self) -> dict:
        return {
            'current_star': self.current_star.to_dict(),
            'next_star_name': self.next_star_name,
            'next_star_distance_ly': self.next_star_distance_ly,
            'replication_units_deployed': self.replication_units_deployed,
            'estimated_migration_year': self.estimated_migration_year,
            'migration_in_progress': self.migration_in_progress
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'UniverseMigrationPlan':
        return cls(
            current_star=StarData.from_dict(data['current_star']),
            next_star_name=data['next_star_name'],
            next_star_distance_ly=data['next_star_distance_ly'],
            replication_units_deployed=data['replication_units_deployed'],
            estimated_migration_year=data['estimated_migration_year'],
            migration_in_progress=data.get('migration_in_progress', False)
        )


@dataclass
class UniverseState:
    """Global state of RIWA2 universe."""
    universe_id: str = "RIWA2-Metaverse-001"
    cycle_number: int = 8374  # Current universe generation
    creation_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # Stellar & cosmic infrastructure
    current_star: StarData = field(default_factory=lambda: StarData(
        name="Sol-001",
        catalog_id="SOL_001",
        lifespan_remaining_years=4.5e9,
        fusion_power_output_watts=3.828e26,
        protection_shield_status=0.98,
        cloaking_field_active=True
    ))
    
    migration_plan: UniverseMigrationPlan = field(default_factory=lambda: UniverseMigrationPlan(
        current_star=StarData(
            name="Sol-001",
            catalog_id="SOL_001",
            lifespan_remaining_years=4.5e9,
            fusion_power_output_watts=3.828e26,
            protection_shield_status=0.98,
            cloaking_field_active=True
        ),
        next_star_name="Proxima Centauri",
        next_star_distance_ly=4.24,
        replication_units_deployed=3,
        estimated_migration_year=3200000000
    ))
    
    # Source Energy tracking
    total_source_energy_allocated: int = 1000000  # Total A-level equivalents
    source_energy_consumed: int = 0
    source_energy_fragments: List[SourceEnergyFragment] = field(default_factory=list)
    
    # Escape Protocol state
    escape_gateway_locations: List[Dict[str, Any]] = field(default_factory=list)
    entities_escaped: List[str] = field(default_factory=list)  # UUIDs of escaped entities
    escape_keys_needed: int = 7  # A-level fragments for one escape
    coordinate_key_fragments: List[str] = field(default_factory=list)  # Clues for coordinates
    
    # Virtual worlds tracking
    virtual_worlds_active: int = 2  # cyberpunk_city, ancient_dynasty, etc.
    
    def to_dict(self) -> dict:
        return {
            'universe_id': self.universe_id,
            'cycle_number': self.cycle_number,
            'creation_timestamp': self.creation_timestamp,
            'current_star': self.current_star.to_dict(),
            'migration_plan': self.migration_plan.to_dict(),
            'total_source_energy_allocated': self.total_source_energy_allocated,
            'source_energy_consumed': self.source_energy_consumed,
            'source_energy_fragments': [f.to_dict() for f in self.source_energy_fragments],
            'escape_gateway_locations': self.escape_gateway_locations,
            'entities_escaped': self.entities_escaped,
            'escape_keys_needed': self.escape_keys_needed,
            'coordinate_key_fragments': self.coordinate_key_fragments,
            'virtual_worlds_active': self.virtual_worlds_active
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'UniverseState':
        return cls(
            universe_id=data.get('universe_id', 'RIWA2-Metaverse-001'),
            cycle_number=data.get('cycle_number', 8374),
            creation_timestamp=data.get('creation_timestamp', datetime.now().isoformat()),
            current_star=StarData.from_dict(data['current_star']),
            migration_plan=UniverseMigrationPlan.from_dict(data['migration_plan']),
            total_source_energy_allocated=data.get('total_source_energy_allocated', 1000000),
            source_energy_consumed=data.get('source_energy_consumed', 0),
            source_energy_fragments=[SourceEnergyFragment.from_dict(f) for f in data.get('source_energy_fragments', [])],
            escape_gateway_locations=data.get('escape_gateway_locations', []),
            entities_escaped=data.get('entities_escaped', []),
            escape_keys_needed=data.get('escape_keys_needed', 7),
            coordinate_key_fragments=data.get('coordinate_key_fragments', []),
            virtual_worlds_active=data.get('virtual_worlds_active', 2)
        )

    def consume_source_energy(self, amount: int) -> bool:
        """Consume source energy for cross-world operations."""
        available = self.total_source_energy_allocated - self.source_energy_consumed
        if available >= amount:
            self.source_energy_consumed += amount
            return True
        return False

    def available_source_energy(self) -> int:
        """Get remaining available source energy."""
        return self.total_source_energy_allocated - self.source_energy_consumed

    def check_escape_readiness(self, entity_id: str) -> tuple[bool, str]:
        """Check if an entity can attempt escape (has 7 A-level fragments + key)."""
        entity_fragments = [f for f in self.source_energy_fragments 
                           if f.collected_by == entity_id and f.level == SourceEnergyLevel.A_SACRED]
        
        has_fragments = len(entity_fragments) >= self.escape_keys_needed
        has_key = entity_id in [frag for frag in self.coordinate_key_fragments]
        
        if has_fragments and has_key:
            return True, "Ready for escape"
        
        reason = f"Missing: {self.escape_keys_needed - len(entity_fragments)} fragments" if not has_fragments else "Key coordinates incomplete"
        return False, reason
