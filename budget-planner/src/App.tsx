import { Container, Button } from 'react-bootstrap';
import { BudgetCard } from './components/BudgetCard';
import { FaPlus } from 'react-icons/fa';

function App() {
  return (
    <div className="app-background">
      <Container className="my-4">
        <div className="d-flex justify-content-between align-items-center mb-4">
          <h1 className="fw-bold text-primary">Планировщик бюджета</h1>
          <Button variant="outline-primary">
            <FaPlus /> Добавить расход
          </Button>
        </div>
        <BudgetCard title="Продукты" amount={5000} limit={10000} />
        <BudgetCard title="Транспорт" amount={2000} limit={5000} />
        <BudgetCard title="Развлечения" amount={3000} limit={7000} />
      </Container>
    </div>
  );
}

export default App;