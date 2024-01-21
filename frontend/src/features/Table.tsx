import {
  Table,
  TableContainer,
  Paper,
  TableHead,
  TableCell,
  TableRow,
  TableBody,
  Stack,
} from "@mui/material";
import { useGetItemsQuery } from "../app/services/api";

export const KeyValueTable = () => {
  const { data: items, isLoading, error } = useGetItemsQuery();
  console.log(!items);
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Key</TableCell>
            <TableCell align="right">Value</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {error ? (
            <TableRow>
              <TableCell colSpan={2}>
                <Stack sx={{ width: "100%" }} spacing={2}>
                  Error!
                </Stack>
              </TableCell>
            </TableRow>
          ) : isLoading || !items || items.length === 0 ? (
            <TableRow>
              <TableCell colSpan={2}>
                <Stack sx={{ width: "100%" }} spacing={2}>
                  No Data!
                </Stack>
              </TableCell>
            </TableRow>
          ) : (
            items.map(({ key, value }) => (
              <TableRow key={`tableRow_${key}`}>
                <TableCell>{key}</TableCell>
                <TableCell>{value}</TableCell>
              </TableRow>
            ))
          )}
        </TableBody>
      </Table>
    </TableContainer>
  );
};
