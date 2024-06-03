import json

def parse_event(event, entity_name, requirements=[]):
    if isinstance(event, dict):
        # Event is already a dictionary
        #check if all requirements are met:
        for item in requirements:
            # logger.info(f"Requirement {item} in body passed is complete:: ")
            try: 
                exists = event[str(item)]
            except:
                # logger.info(f"Found an exception on {item}:: ")
                return True, str(f"Please ensure you have {item} in the {entity_name}!")
        return True, event
    elif isinstance(event, str):
        try:
            # Attempt to parse string as JSON
            for item in requirements:
                try: 
                    exists = event[item]
                except:
                    return True, f"Please ensure you have {item} in the {entity_name}!"
            event = json.loads(event)
            return True, event
        except json.JSONDecodeError:
            # Not a valid JSON string
            return False, None
    else:
        # Unsupported format
        return False, None