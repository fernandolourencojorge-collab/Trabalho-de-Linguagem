using System;

namespace FaturacaoLoja
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine(" SISTEMA DE FATURAÇÃO - LOJA DE PRODUTOS ALIMENTARES ");
            
            Console.Write("Digite o nome do cliente: ");
            string nome = Console.ReadLine();

            Console.Write("Digite o género do cliente (M/F): ");
            char genero = Convert.ToChar(Console.ReadLine().ToUpper());

            Console.Write("Digite o valor total das compras (Kz): ");
            double valorCompras = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("\n-- Condições de Prioridade --");
            Console.WriteLine("O cliente enquadra-se em alguma categoria prioritária? (Grávida, Idoso(a), Pessoa com deficiência)");
            Console.Write("Possui prioridade? (s/n): ");
            char temPrioridade = Convert.ToChar(Console.ReadLine().ToLower());

            bool prioritario = (temPrioridade == 's');

            double bonus = 0;
            double valorPagar = valorCompras;
            double limiteBonus = 100000.0;

            if (valorCompras > limiteBonus)
            {
                bonus = valorCompras * 0.10; 
                valorPagar = valorCompras - bonus;
            }

            Console.WriteLine("\n                                        ");
            Console.WriteLine("              TALÃO / FATURA              ");
            Console.WriteLine("                                          ");
            Console.WriteLine($"Nome do Cliente: {nome}");
            Console.WriteLine($"Género: {genero}");
            Console.WriteLine($"Valor Inicial das Compras: {valorCompras:N2} Kz");
            
            if (valorCompras > limiteBonus)
            {
                Console.WriteLine($"Bónus Aplicado (10%): {bonus:N2} Kz");
                Console.WriteLine($"Valor Final a Pagar: {valorPagar:N2} Kz");
            }
            else
            {
                Console.WriteLine("Bónus Comercial: Não aplicável (Compras <= 100.000 Kz)");
                Console.WriteLine($"Valor Final a Pagar: {valorPagar:N2} Kz");
            }

            Console.WriteLine("                              ");
            if (prioritario)
            {
                Console.WriteLine("Estado de Atendimento: ATENDIMENTO PRIORITÁRIO ");
            }
            else
            {
                Console.WriteLine("Estado de Atendimento: Atendimento Regular ");
            }
            Console.WriteLine("                            ");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
