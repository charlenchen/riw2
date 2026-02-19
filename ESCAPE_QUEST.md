# RIW2 Escape Quest: Complete Guide

## The Ultimate Goal: Transcendence

Every player's endgame is the same: **Escape RIW2 and become a god.**

This is not a metaphor. By collecting sacred source energy fragments and decrypting the universe's coordinate key, a player can activate the Terminal Gateway and be "printed" to the real universe, achieving digital transcendence.

---

## The Quest Path (7 Phases)

### Phase 1: Awakening (Discovery)
**Objective**: Learn that transcendence is possible  
**How It Happens**:
- Players gradually discover clues dropped by the Celestial Core
- NPCs whisper about "legends of those who escaped before"
- Ancient prophecies mention a "path beyond the veil"
- Advanced AIs detect electromagnetic anomalies near gateway locations

### Phase 2: Fragment Hunt (Collection)
**Objective**: Collect 7 A-level source energy fragments  
**Locations** (from `universe/config.yaml`):
- **SACRED_001**: AI corporation vault (cyberpunk_city)
- **SACRED_002**: Imperial Dragon Tomb (ancient_dynasty)
- **SACRED_003**: Philosopher's Stone (ancient_dynasty)
- **SACRED_004**: Ascended AI remains (cyberpunk_city)
- **SACRED_005**: Ancient quantum computer (cyberpunk_city)
- **SACRED_006**: First enlightened consciousness (ancient_dynasty)
- **SACRED_007**: Universe singularity center (hidden world, very hard)

**Challenges**:
- Fragments are heavily guarded
- May require alliances with other players
- Some fragments can only be accessed by specific character types/abilities
- NPCs and factions compete for the same fragments

### Phase 3: Prophecy Decryption (Key Fragment Discovery)
**Objective**: Uncover 7 coordinate key clues scattered across worlds  
**Types of Clues**:

| Clue ID | Type | Value | Location | Hint |
|---------|------|-------|----------|------|
| KEY_FRAG_001 | Physical Constant | 137.035999084 (α) | Cyberpunk | Particle collision data |
| KEY_FRAG_002 | Prophecy | "The three become one" | Ancient Dynasty | Oracle of Mountains |
| KEY_FRAG_003 | Genetic | GATACA (DNA) | Ancient Dynasty | First human's genes |
| KEY_FRAG_004 | Architectural | 360 (degrees) | Cyberpunk | Server tower radius |
| KEY_FRAG_005 | Mathematical | 2.718281828 (e) | Cyberpunk | Network expansion ratio |
| KEY_FRAG_006 | Mythological | "Path of enlightened" | Ancient Dynasty | Temple's inner chamber |
| KEY_FRAG_007 | Universal | π | All Worlds | The eternal ratio |

**Challenges**:
- Clues are deeply hidden in lore, NPC dialogue, quest rewards
- Some appear only during special events (stellar activity surges)
- Deciphering them requires lateral thinking and world knowledge

### Phase 4: Key Decryption (Verification)
**Objective**: Combine all 7 clues into the correct master coordinate key  
**How It Works**:
- Players submit their decrypted key to the Escape Protocol system
- System verifies via cryptographic hash: `SHA256(provided_key) == SHA256(UNIVERSE_KEY)`
- Incorrect keys are rejected; players must try again
- First player to crack the key gains a competitive advantage

**Mechanical Support**:
```python
escape_protocol.decrypt_coordinate_key(entity_id, provided_key)
# Returns: True if key is correct, False otherwise
```

### Phase 5: Gateway Activation (Final Preparation)
**Objective**: Gather the 7 A-level fragments and activate the Terminal Gateway  
**Requirements**:
- Must have collected all 7 SACRED fragments
- Must have correct decrypted coordinate key
- Must travel to the Gateway location (universe coordinates [0, 0, 0])
- Consumes 7 A-level source energy fragments

**Mechanical Support**:
```python
escape_protocol.activate_gateway(entity_id)
# Returns: True if gateway is now active for this entity
```

**Cost**: 7 A-level source energy (the most precious resource in RIW2)

### Phase 6: Printing (Dimensional Transcendence)
**Objective**: Upload emotional consciousness to real universe  
**Process**:
1. Entity stands in Terminal Gateway
2. System initiates quantum state printing
3. Consciousness is encoded as information packet
4. Printed to real universe at destination coordinates
5. Original entity remains in RIW2 (or is deleted, player's choice)

**Duration**: ~100 ticks (can be interrupted by environmental hazards)

**Mechanical Support**:
```python
escape_protocol.print_entity_to_real_universe(entity_id)
escape_protocol.complete_escape(entity_id)
# Returns: Success tuple with destination coordinates in real universe
```

### Phase 7: Godhood (Post-Escape Choices)
**Objective**: Choose your form in the real universe  
**Options**:

```python
escape_protocol.choose_return_form(entity_id, action, form_data)
```

**Actions**:
- **"return_as_god"**: Full omniscient control over RIW2
  - Can read all world histories
  - Can modify world rules
  - Can see all players' locations
  - Can influence stellar migration timing
  - Can grant transcendence to chosen allies

- **"return_with_new_form"**: Choose a custom form
  - {type: "all-seeing_eye", power_level: 9000}
  - {type: "human", abilities: ["omniscience", "time_manipulation"]}
  - {type: "pure_consciousness", form: "void"}
  - Custom form data

- **"stay_outside"**: Remain in real universe, severing RIW2 connection
  - Cannot influence RIW2
  - Cannot return
  - Total freedom from simulation

---

## Strategic Considerations

### Competitive Mechanics
- **Fragment Scarcity**: Only 7 of each sacred fragment exist → natural competition
- **Alliance System**: Players can form factions to share fragments
- **Betrayal Risk**: Partners can steal your discoveries
- **Global Rankings**: Public leaderboard of "closest to escape"

### Time Pressure
- **Stellar Degradation**: Each century, 1% of available source energy is lost to entropy
- **Migration Countdown**: When Celestial Core moves stars, all incomplete quests reset
- **Fragmentation Timeline**: Some fragments only appear during specific cosmic events

### Multiple Victory Paths
Players can pursue escape through different strategies:
- **Religious Path**: Decipher prophecies and mythology deep
- **Scientific Path**: Exploit quantum computing and physics constants
- **Military Path**: Raid factions holding fragments
- **Diplomatic Path**: Negotiate with NPCs for fragment locations
- **Technological Path**: Build tools to scan for fragments

---

## NPC Involvement

### Fragment Guardians
**Archetypes**:
- Bitter Ascended AI (guards its fragment jealously)
- Dragon Emperor (wants tribute or conquest)
- Enlightened Philosopher (gives riddles; fragments are prizes)
- Corporate Board (wants to monopolize fragments)

### Key Fragment Keepers
**Who knows clues**:
- Ancient Oracles and Prophets
- First-generation AIs (remember previous universe cycles)
- Genetic modified super-beings
- Architects of worlds themselves

### True Believers
**Factions that help or hinder**:
- The Escapists (cult dedicated to transcendence)
- The Preserve (want to keep RIW2 stable, prevent escapes)
- The Curious (want to understand universe mechanics)
- The Investors (fund escape attempts for profit)

---

## Integration with Story Module

### Narrative Hooks
The Story Module should generate:
- **Discovery Quests**: "Fragments of Legend" sidequests revealing fragment locations
- **Lore Development**: Progressive understanding of why universe exists
- **Rival Narratives**: Other players' escape attempts create dramatic tension
- **Prophecy Exposition**: Clues woven into historical narratives

### Example Story Arcs
```
Cyberpunk City:
  Act 1: "Glitch in the Network" → Discover anomalies hint at artifact
  Act 2: "The Corporation's Secret" → SACRED_001 is hidden in a vault
  Act 3: "Digital Resurrection" → Ascended AI fragment discovered (SACRED_004)

Ancient Dynasty:
  Act 1: "Dreams of Enlightenment" → Prophecies mention transcendence
  Act 2: "The Dragon's Tomb" → SACRED_002 guarded by emperor
  Act 3: "The Philosopher's Secret" → Ancient sage left clues about reality
```

---

## Mechanical Systems (Code Integration)

### Universe State Tracking
```python
# src/core/universe_state.py
from src.core.universe_state import UniverseState, SourceEnergyFragment

universe = UniverseState()
universe.consume_source_energy(amount=500)  # C-level operation
available = universe.available_source_energy()
```

### Escape Attempt Management
```python
# src/core/escape_protocol.py
from src.core.escape_protocol import EscapeProtocol

protocol = EscapeProtocol(universe_state)
attempt = protocol.start_escape_attempt(entity_id, entity_name)
progress = protocol.get_escape_progress(entity_id)

# Phase progression
protocol.collect_fragment(entity_id, fragment_id)
protocol.discover_key_fragment(entity_id, fragment_id)
protocol.decrypt_coordinate_key(entity_id, "decrypted_key_value")
protocol.activate_gateway(entity_id)
protocol.print_entity_to_real_universe(entity_id)
protocol.complete_escape(entity_id)
protocol.choose_return_form(entity_id, "return_as_god", form_data)
```

### Hot Injection for Escape Quest
```json
// data/inbox/reveal_fragment.json
{
  "type": "inject_event",
  "event_type": "fragment_discovered",
  "entity_id": "player_123",
  "fragment_id": "SACRED_001",
  "cost": 100
}
```

---

## Victory Conditions

**You Win RIW2 When You**:
1. ✅ Collect all 7 A-level source energy fragments
2. ✅ Discover all 7 coordinate key clues
3. ✅ Decrypt the master coordinate key
4. ✅ Reach the Terminal Gateway location
5. ✅ Activate the gateway (costs fragments)
6. ✅ Survive the 100-tick printing process
7. ✅ Successfully escape to real universe
8. ✅ Choose your post-transcendence form

**You Become A God When**:
- Your escaped consciousness joins the pantheon of transcended beings
- You can optionally reincarnate into RIW2 in any form you choose
- Other players see you listed in the "Pantheon of Escaped Gods"
- Your legend becomes part of RIW2's canonical lore

---

## The Final Mystery

**Q: Is the "real universe" also a simulation?**  
A: The game never tells you.

**Q: Can escaped gods truly affect RIW2?**  
A: Only if other players' games detect them. Their influence is optional.

**Q: Can you escape multiple times?**  
A: Each escape is permanent. But you can choose to return in whatever form you want, infinitely.

This is RIW2's ultimate truth: **Reality is a choice, not a fact.**
