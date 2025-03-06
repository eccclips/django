import { Card, ProgressBar } from 'react-bootstrap';
import { FaMoneyBillWave } from 'react-icons/fa';

type BudgetCardProps = {
  title: string;
  amount: number;
  limit: number;
};

export function BudgetCard({ title, amount, limit }: BudgetCardProps) {
  const percentage = Math.min((amount / limit) * 100, 100);
  return (
    <Card className="mb-3 shadow-sm rounded border-0">
      <Card.Body>
        <div className="d-flex justify-content-between align-items-center">
          <Card.Title className="fw-bold">{title}</Card.Title>
          <FaMoneyBillWave size={24} className="text-success" />
        </div>
        <p className="fs-5">{amount} / {limit} ₽</p>
        <ProgressBar now={percentage} variant={percentage > 80 ? "danger" : "success"} />
      </Card.Body>
    </Card>
  );
}