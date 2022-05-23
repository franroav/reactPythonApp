import React, {
  Fragment,
  useState,
  useEffect,
  useRef,
  PureComponent,
} from "react";

import {
  BarChart,
  Bar,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const data = [];
/*=============================================
        =       COMPONENTE BARCHART          =
  =============================================*/
const ChartBar = (props) => {
  const demand = props.demand;
  if (demand.length) {
    const actualMonth = demand.reduce(
      (total, fuel) => total + fuel.total_count,
      0
    );
    const lastMonth = demand.reduce(
      (total, fuel) => total + fuel.total_count_previous_month,
      0
    );
    data.push({ date: "04-2022", services: lastMonth });
    data.push({ date: "05-2022", services: actualMonth });
    return (
      <>
        <BarChart width={1200} height={600} data={data}>
          <Bar dataKey="services" fill="green" />
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="date" />
          <YAxis />
        </BarChart>
      </>
    );
  }
  return <></>;
  // console.log('datakeyx: ' + dataKeyX);
  // console.log(report);
  // const useQuantity = report === 'dailySales' || report === 'monthlySales';
  // console.log('useqty: ' + useQuantity);
};

export default ChartBar;
