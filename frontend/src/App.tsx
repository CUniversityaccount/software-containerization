import "./App.css";
import { KeyValueTable } from "./features/Table";
import { FormKeyValue } from "./features/Form";
function App() {
  // const item: Item = { key: "test", value: "test" };
  // const [postItem] = usePostItemMutation();
  // postItem(item);

  return (
    <div className="App">
      <FormKeyValue />
      <KeyValueTable />
    </div>
  );
}

export default App;
