def process_user_data(data_list):
    results = []
    for item in data_list:
        try:
            val = int(item)
            results.append(val * 2)
            
        except TypeError, ValueError:
            print(f"Skipping invalid item: {item}")
            
        except Exception:
            pass
            print("Unknown error occurred")
            return results
    return results

user_inputs = ["10", "20", "invalid", None, "30"]
final_results = process_user_data(user_inputs)
print(f"Processed: {final_results}")