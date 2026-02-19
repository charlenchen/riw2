"""
Escape Protocol: The mechanism by which entities transcend RIW2 and become gods.
Implements the terminal gateway and dimensional printing system.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from datetime import datetime
from uuid import uuid4
import hashlib
from enum import Enum


class EscapeStatus(Enum):
    """Status of an escape attempt."""
    NOT_STARTED = "not_started"
    FRAGMENTS_COLLECTING = "collecting_fragments"
    KEY_DECRYPTING = "decrypting_key"
    GATEWAY_OPENING = "opening_gateway"
    PRINTING = "printing_to_real_universe"
    ESCAPED = "escaped"
    FAILED = "failed"


@dataclass
class CoordinateKeyFragment:
    """
    A piece of the coordinate key needed to open the terminal gateway.
    Hidden in physical constants, DNA sequences, architecture dimensions, etc.
    """
    fragment_id: str
    hidden_in_world: str  # Which world contains this clue
    clue_type: str  # "physical_constant", "prophecy", "genetic", "architectural"
    clue_value: str  # The actual data/number
    discovery_requirements: Dict[str, Any]  # What player must do to unlock it
    discovered_at: Optional[str] = None
    discovered_by: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            'fragment_id': self.fragment_id,
            'hidden_in_world': self.hidden_in_world,
            'clue_type': self.clue_type,
            'clue_value': self.clue_value,
            'discovery_requirements': self.discovery_requirements,
            'discovered_at': self.discovered_at,
            'discovered_by': self.discovered_by
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CoordinateKeyFragment':
        return cls(
            fragment_id=data['fragment_id'],
            hidden_in_world=data['hidden_in_world'],
            clue_type=data['clue_type'],
            clue_value=data['clue_value'],
            discovery_requirements=data['discovery_requirements'],
            discovered_at=data.get('discovered_at'),
            discovered_by=data.get('discovered_by')
        )


@dataclass
class TerminalGateway:
    """
    The portal through which entities are printed to the real universe.
    Only one can be activated per cycle.
    """
    gateway_id: str = field(default_factory=lambda: str(uuid4()))
    location_world: str = "universe_singularity"
    location_coordinates: Dict[str, float] = field(default_factory=lambda: {"x": 0.0, "y": 0.0, "z": 0.0})
    
    # Activation state
    is_active: bool = False
    activation_time: Optional[str] = None
    activated_by_entity: Optional[str] = None
    
    # Properties
    source_energy_cost: int = 7  # Requires 7 A-level fragments
    printing_capacity: int = 1  # Can print one entity at a time
    
    # Printing queue
    entities_in_queue: List[str] = field(default_factory=list)  # Entity UUIDs waiting
    current_printing_entity: Optional[str] = None
    printing_progress: float = 0.0  # 0.0 to 1.0
    
    def to_dict(self) -> dict:
        return {
            'gateway_id': self.gateway_id,
            'location_world': self.location_world,
            'location_coordinates': self.location_coordinates,
            'is_active': self.is_active,
            'activation_time': self.activation_time,
            'activated_by_entity': self.activated_by_entity,
            'source_energy_cost': self.source_energy_cost,
            'printing_capacity': self.printing_capacity,
            'entities_in_queue': self.entities_in_queue,
            'current_printing_entity': self.current_printing_entity,
            'printing_progress': self.printing_progress
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'TerminalGateway':
        return cls(
            gateway_id=data.get('gateway_id', str(uuid4())),
            location_world=data.get('location_world', 'universe_singularity'),
            location_coordinates=data.get('location_coordinates', {'x': 0.0, 'y': 0.0, 'z': 0.0}),
            is_active=data.get('is_active', False),
            activation_time=data.get('activation_time'),
            activated_by_entity=data.get('activated_by_entity'),
            source_energy_cost=data.get('source_energy_cost', 7),
            printing_capacity=data.get('printing_capacity', 1),
            entities_in_queue=data.get('entities_in_queue', []),
            current_printing_entity=data.get('current_printing_entity'),
            printing_progress=data.get('printing_progress', 0.0)
        )


@dataclass
class EscapeAttempt:
    """Record of an entity's attempt to escape RIW2."""
    attempt_id: str = field(default_factory=lambda: str(uuid4()))
    entity_id: str = ""
    entity_name: str = ""
    start_time: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # Progress tracking
    status: EscapeStatus = EscapeStatus.NOT_STARTED
    
    # Fragment collection
    collected_a_level_fragments: List[str] = field(default_factory=list)  # Fragment IDs
    
    # Key decryption
    discovered_key_fragments: List[str] = field(default_factory=list)  # Fragment IDs
    final_coordinate_key: Optional[str] = None
    
    # Gateway access
    gateway_id: Optional[str] = None
    gateway_activation_time: Optional[str] = None
    
    # Printing
    printing_start_time: Optional[str] = None
    printing_complete_time: Optional[str] = None
    printing_destination: Optional[str] = None  # Name of real universe location
    
    # Result
    success: bool = False
    result_message: str = ""
    
    # Post-escape choices
    post_escape_action: Optional[str] = None  # "return_as_god", "return_with_new_form", "stay_outside"
    new_form_chosen: Optional[Dict[str, Any]] = None  # Description of new form if returning
    
    def to_dict(self) -> dict:
        return {
            'attempt_id': self.attempt_id,
            'entity_id': self.entity_id,
            'entity_name': self.entity_name,
            'start_time': self.start_time,
            'status': self.status.value,
            'collected_a_level_fragments': self.collected_a_level_fragments,
            'discovered_key_fragments': self.discovered_key_fragments,
            'final_coordinate_key': self.final_coordinate_key,
            'gateway_id': self.gateway_id,
            'gateway_activation_time': self.gateway_activation_time,
            'printing_start_time': self.printing_start_time,
            'printing_complete_time': self.printing_complete_time,
            'printing_destination': self.printing_destination,
            'success': self.success,
            'result_message': self.result_message,
            'post_escape_action': self.post_escape_action,
            'new_form_chosen': self.new_form_chosen
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'EscapeAttempt':
        return cls(
            attempt_id=data.get('attempt_id', str(uuid4())),
            entity_id=data['entity_id'],
            entity_name=data['entity_name'],
            start_time=data.get('start_time', datetime.now().isoformat()),
            status=EscapeStatus(data.get('status', 'not_started')),
            collected_a_level_fragments=data.get('collected_a_level_fragments', []),
            discovered_key_fragments=data.get('discovered_key_fragments', []),
            final_coordinate_key=data.get('final_coordinate_key'),
            gateway_id=data.get('gateway_id'),
            gateway_activation_time=data.get('gateway_activation_time'),
            printing_start_time=data.get('printing_start_time'),
            printing_complete_time=data.get('printing_complete_time'),
            printing_destination=data.get('printing_destination'),
            success=data.get('success', False),
            result_message=data.get('result_message', ''),
            post_escape_action=data.get('post_escape_action'),
            new_form_chosen=data.get('new_form_chosen')
        )


class EscapeProtocol:
    """
    Core system handling the escape mechanism.
    Coordinates fragment collection, key decryption, gateway activation, and printing.
    """

    def __init__(self, universe_state):
        self.universe_state = universe_state
        self.escape_attempts: Dict[str, EscapeAttempt] = {}
        self.coordinate_key_formula = self._initialize_key_formula()
        self.terminal_gateway = TerminalGateway()
        
    def _initialize_key_formula(self) -> str:
        """
        Return the master key formula (hidden in the codebase).
        In a real game, this would be obscured in physical constants or world lore.
        """
        # Example: hash of combined coordinate fragments
        # In practice, this could be derived from:
        # - Fine structure constant (α ≈ 1/137)
        # - Planck constant derivatives
        # - Prophecies in ancient mythology
        # - Genetic sequences of first life forms
        return "key_formula_locked_in_universe_core"

    def start_escape_attempt(self, entity_id: str, entity_name: str) -> EscapeAttempt:
        """Initialize a new escape attempt for an entity."""
        attempt = EscapeAttempt(entity_id=entity_id, entity_name=entity_name)
        self.escape_attempts[attempt.attempt_id] = attempt
        attempt.status = EscapeStatus.FRAGMENTS_COLLECTING
        return attempt

    def collect_fragment(self, entity_id: str, fragment_id: str) -> bool:
        """
        Record that an entity has collected a source energy A-level fragment.
        """
        for fragment in self.universe_state.source_energy_fragments:
            if fragment.id == fragment_id:
                fragment.collected_by = entity_id
                fragment.collection_timestamp = datetime.now().isoformat()
                
                # Add to any active escape attempt for this entity
                for attempt in self.escape_attempts.values():
                    if attempt.entity_id == entity_id:
                        if fragment_id not in attempt.collected_a_level_fragments:
                            attempt.collected_a_level_fragments.append(fragment_id)
                        return True
        return False

    def discover_key_fragment(self, entity_id: str, fragment_id: str) -> bool:
        """
        Record that an entity has discovered a coordinate key clue.
        """
        for key_frag in self.universe_state.coordinate_key_fragments:
            if key_frag == fragment_id:  # Simplified; in reality would check CoordinateKeyFragment objects
                for attempt in self.escape_attempts.values():
                    if attempt.entity_id == entity_id:
                        if fragment_id not in attempt.discovered_key_fragments:
                            attempt.discovered_key_fragments.append(fragment_id)
                        attempt.status = EscapeStatus.KEY_DECRYPTING
                        return True
        return False

    def decrypt_coordinate_key(self, entity_id: str, provided_key: str) -> bool:
        """
        Attempt to decrypt the master coordinate key using collected clues.
        """
        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id:
                # Verify the key by checking against our formula
                if self._verify_key(provided_key):
                    attempt.final_coordinate_key = provided_key
                    attempt.status = EscapeStatus.GATEWAY_OPENING
                    return True
        return False

    def _verify_key(self, key: str) -> bool:
        """
        Verify if the provided key matches the universe's escape coordinate.
        (In production, would use cryptographic verification.)
        """
        # Simplified: check if key matches the hash of expected clues
        expected = hashlib.sha256(self.coordinate_key_formula.encode()).hexdigest()
        return hashlib.sha256(key.encode()).hexdigest() == expected

    def activate_gateway(self, entity_id: str) -> bool:
        """
        Activate the terminal gateway for this entity.
        Consumes 7 A-level source energy fragments.
        """
        if self.terminal_gateway.is_active:
            return False  # Gateway already active

        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id and attempt.status == EscapeStatus.GATEWAY_OPENING:
                # Check fragment count
                if len(attempt.collected_a_level_fragments) < 7:
                    return False
                
                # Consume source energy
                if not self.universe_state.consume_source_energy(7):
                    return False

                # Activate gateway
                self.terminal_gateway.is_active = True
                self.terminal_gateway.activation_time = datetime.now().isoformat()
                self.terminal_gateway.activated_by_entity = entity_id
                self.terminal_gateway.entities_in_queue.append(entity_id)
                attempt.gateway_activation_time = self.terminal_gateway.activation_time
                attempt.status = EscapeStatus.PRINTING
                return True

        return False

    def print_entity_to_real_universe(self, entity_id: str) -> tuple[bool, str]:
        """
        Begin printing the entity to real universe.
        Simulates quantum information transfer and dimensional transcendence.
        """
        if not self.terminal_gateway.is_active or self.terminal_gateway.current_printing_entity != entity_id:
            return False, "Gateway not ready or entity not in printing slot"

        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id and attempt.status == EscapeStatus.PRINTING:
                attempt.printing_start_time = datetime.now().isoformat()
                attempt.printing_destination = f"RealUniverse_Coordinates_{self._generate_destination()}"
                return True, "Printing initiated"

        return False, "No active escape attempt for entity"

    def complete_escape(self, entity_id: str) -> tuple[bool, str]:
        """
        Mark an entity as successfully escaped.
        They can now choose their post-escape form and return.
        """
        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id and attempt.status == EscapeStatus.PRINTING:
                attempt.printing_complete_time = datetime.now().isoformat()
                attempt.success = True
                attempt.status = EscapeStatus.ESCAPED
                attempt.result_message = f"Successfully transcended to real universe at {attempt.printing_destination}"
                
                # Remove from gateway queue
                if entity_id in self.terminal_gateway.entities_in_queue:
                    self.terminal_gateway.entities_in_queue.remove(entity_id)
                self.terminal_gateway.current_printing_entity = None
                
                # Record in universe state
                self.universe_state.entities_escaped.append(entity_id)
                
                return True, attempt.result_message

        return False, "No escape attempt found"

    def choose_return_form(self, entity_id: str, action: str, form_data: Optional[Dict[str, Any]] = None) -> bool:
        """
        After escaping, entity can choose to return to RIW2 in a new form.
        
        Options:
        - "return_as_god": Full control over RIW2 universe
        - "return_with_new_form": Return in custom form (god, human, AI, etc.)
        - "stay_outside": Remain in real universe
        """
        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id and attempt.success:
                attempt.post_escape_action = action
                if form_data:
                    attempt.new_form_chosen = form_data
                return True
        return False

    def _generate_destination(self) -> str:
        """Generate a realistic-sounding real universe coordinate."""
        import random
        return f"Alpha_Centauri_{random.randint(1000, 9999)}"

    def get_escape_progress(self, entity_id: str) -> Dict[str, Any]:
        """Get current progress of an entity's escape attempt."""
        for attempt in self.escape_attempts.values():
            if attempt.entity_id == entity_id:
                return {
                    'status': attempt.status.value,
                    'fragments_collected': len(attempt.collected_a_level_fragments),
                    'fragments_needed': 7,
                    'key_fragments_discovered': len(attempt.discovered_key_fragments),
                    'has_coordinate_key': attempt.final_coordinate_key is not None,
                    'gateway_active': self.terminal_gateway.is_active and self.terminal_gateway.activated_by_entity == entity_id,
                    'success': attempt.success
                }
        return None
